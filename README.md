# Satellite Orbit Simulation

## Overview

This project simulates the motion of a satellite orbiting the Earth, accounting for:
- Earth's gravitational field
- Atmospheric drag
- Gravitational perturbations from the Moon
- Real-time control of the satellite's orientation and engine power

The simulation also provides visualization and real-time updates on the satellite's status.

---

# Моделирование орбитального движения спутника

## Общий обзор

Проект моделирует движение космического аппарата на орбите Земли, с учетом:
- Гравитационного поля Земли
- Сопротивления атмосферы
- Возмущений от гравитации Луны
- Возможности реального управления ориентацией и двигателем

Модель обеспечивает визуализацию и обновление всех данных в реальном времени.

## Usage / Использование

1. Run the script to initiate the simulation and visualization.
2. Use `set_engine_power` to set the engine thrust.
3. Use `set_engine_direction` to adjust the engine direction (as a normalized vector).
4. Monitor the real-time visualization and data output.

1. Запустите скрипт для запуска модели и визуализации.
2. Используйте `set_engine_power` для установки тяги двигателя.
3. Используйте `set_engine_direction` для управления направлением двигателя (как нормированный вектор).
4. Наблюдайте за визуализацией и данными в реальном времени.

## Requirements / Требования

- Python 3.8+
- `numpy`
- `matplotlib`

---
