# 🐢 Turtle Crossing Game

A Frogger-style arcade game built with Python's Turtle module. Guide the turtle across a busy road while avoiding moving cars!

---

## 🎯 Project Overview

The player controls a turtle that must cross a busy road filled with moving cars. Each successful crossing increases the level, making the cars move faster. The game ends when the turtle gets hit by a car.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| **Player Movement** | Move up, down, left, right using arrow keys |
| **Car Generation** | Random cars spawn at different speeds |
| **Collision Detection** | If car hits turtle → lose a life |
| **Level Progression** | Each level = more cars, faster speed |
| **Score Tracking** | Track levels completed |
| **Game Over** | When turtle gets hit |

---

## 📁 Project Structure
ex02/
├── screen.py # Game loop

├── object_turtle.py # Player class (turtle)

├── car_manager.py # Car class (spawn, move)

├── level.py #level tracking

├── README.md # Documentation

└── .gitignore # Ignored files


---

## 🛠️ Technologies Used

- **Python 3.12.3**
- **Turtle Graphics** – Game rendering
- **Random Module** – Car generation
- **OOP Principles** – Classes for Player, Car, Scoreboard

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone git@github.com:kama13a/TurtleCrossing.git
cd TurtleCrossing
python main.py