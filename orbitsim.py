import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Физические константы
G = 6.67430e-11  # гравитационная постоянная, м^3/(кг*с^2)
M_EARTH = 5.972e24  # масса Земли, кг
R_EARTH = 6371e3  # радиус Земли, м
M_MOON = 7.348e22  # масса Луны, кг
R_MOON = 384400e3  # расстояние до Луны, м
ATM_DENSITY = 1.2  # плотность атмосферы на уровне Земли, кг/м^3
ATM_SCALE_HEIGHT = 8500  # масштаб высоты атмосферы, м

# Начальные условия
satellite_mass = 500  # масса спутника, кг
position = np.array([7000e3, 0])  # начальная позиция, м
velocity = np.array([0, 7.5e3])  # начальная скорость, м/с

dt = 1  # временной шаг, с
engine_power = 0  # мощность двигателя, Н
engine_direction = np.array([1, 0])  # направление двигателя

# Лунные возмущения (статическая позиция для простоты)
moon_position = np.array([R_MOON, 0])

# Запись данных для визуализации
positions = [position.copy()]

# Функция для вычисления силы гравитации
def gravitational_force(mass1, mass2, pos1, pos2):
    r = np.linalg.norm(pos2 - pos1)
    if r == 0:
        return np.array([0, 0])
    force_magnitude = G * mass1 * mass2 / r**2
    force_direction = (pos2 - pos1) / r
    return force_magnitude * force_direction

# Функция для учета атмосферного сопротивления
def atmospheric_drag(velocity, position):
    altitude = np.linalg.norm(position) - R_EARTH
    if altitude < 0:
        return np.array([0, 0])
    density = ATM_DENSITY * np.exp(-altitude / ATM_SCALE_HEIGHT)
    drag_coefficient = 2.2  # коэффициент сопротивления
    cross_sectional_area = 4  # м^2
    drag_force_magnitude = 0.5 * density * drag_coefficient * cross_sectional_area * np.linalg.norm(velocity)**2
    return -drag_force_magnitude * velocity / np.linalg.norm(velocity)

# Основной цикл моделирования
def update():
    global position, velocity, engine_power, engine_direction
    # Гравитация Земли
    gravity_force = gravitational_force(satellite_mass, M_EARTH, position, np.array([0, 0]))
    
    # Гравитация Луны
    moon_gravity_force = gravitational_force(satellite_mass, M_MOON, position, moon_position)

    # Атмосферное сопротивление
    drag_force = atmospheric_drag(velocity, position)

    # Сила от двигателя
    engine_force = engine_power * engine_direction

    # Итоговое ускорение
    total_force = gravity_force + moon_gravity_force + drag_force + engine_force
    acceleration = total_force / satellite_mass

    # Обновление скорости и позиции
    velocity += acceleration * dt
    position += velocity * dt

    # Запись данных
    positions.append(position.copy())

# Визуализация
fig, ax = plt.subplots()
ax.set_xlim(-1.5 * R_MOON, 1.5 * R_MOON)
ax.set_ylim(-1.5 * R_MOON, 1.5 * R_MOON)
ax.set_aspect('equal')

satellite_dot, = ax.plot([], [], 'ro')

# Анимация
def animate(frame):
    update()
    satellite_dot.set_data(position[0], position[1])
    return satellite_dot,

ani = FuncAnimation(fig, animate, frames=1000, interval=dt * 1000, blit=True)

# Интерфейс управления
def set_engine_power(power):
    global engine_power
    engine_power = power

def set_engine_direction(direction):
    global engine_direction
    engine_direction = direction / np.linalg.norm(direction)

# Вывод информации на экран
def display_info():
    altitude = np.linalg.norm(position) - R_EARTH
    print(f"Позиция: {position} м")
    print(f"Скорость: {velocity} м/с")
    print(f"Высота: {altitude} м")
    print(f"Двигатель: мощность {engine_power} Н, направление {engine_direction}")

plt.show()
