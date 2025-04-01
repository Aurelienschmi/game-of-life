# Game of Life

The **Game of Life** is a simulation based on cellular automata, invented by mathematician John Conway. This project implements the Game of Life in Python, with simple rules to simulate the evolution of a grid of living and dead cells.

---

## Features

- Generate an empty or random grid.
- Apply the rules of the Game of Life:
  - A living cell dies if it has fewer than 2 living neighbors (underpopulation).
  - A living cell dies if it has more than 3 living neighbors (overpopulation).
  - A dead cell becomes alive if it has exactly 3 living neighbors (reproduction).
- Display the grid at each step.
- Automatically stop when all cells are dead.

---

## Project Structure

Here are the main files of the project:

- **`main.py`**: Entry point of the program. Manages the main loop and displays generations.
- **`game.py`**: Contains the main functions to manage the grid, apply the rules, and check cell states.
- **`variables.py`**: Defines the grid dimensions (`rows` and `cols`).

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Aurelienschmi/game-of-life
   cd game-of-life
    ```

2. Make sure you have Python 3 installed on your machine.

3. Run the program:
    ```bash
    python main.py
    ```
    

