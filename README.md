
<img width="609" alt="pic1" src="https://github.com/ramirazodi/a_star_path_optimizer/assets/106940649/d1b8238d-04ad-445f-8d59-1c3c870efcd7">
<img width="608" alt="pic2" src="https://github.com/ramirazodi/a_star_path_optimizer/assets/106940649/dd2305e2-b4d7-471c-913d-14c79ab87fc1">

# A* Pathfinding Visualization

This project implements the A* pathfinding algorithm with a graphical user interface to visualize the algorithm in action. It allows users to set start and end points, draw barriers, and visualize the pathfinding process in a grid layout.

## Features

- Interactive 50x60 grid for setting up pathfinding scenarios.
- Ability to place start and end points on the grid.
- Functionality to draw barriers on the grid to create complex pathfinding scenarios.
- Toggleable real-time visualization of the A* algorithm.
- Clear Grid function to reset the scenario.
- Performance optimizations for scenarios with long barriers or narrow paths.

## How to Use

1. **Starting the Application**: Run `main.py` to start the application.
2. **Setting Points**: Click on a grid cell to set the start point (green cell) and the end point (red cell).
3. **Drawing Barriers**: Click and drag on the grid to draw barriers (black cells).
4. **Pathfinding**:
   - Click the "Start Pathfinding" button to find the shortest path from start to end.
   - Use the "Toggle Visualization" button to turn on/off the real-time visualization of the algorithm.
5. **Resetting the Grid**: Use the "Clear Grid" button to clear the grid and set up a new scenario.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

To run the application, ensure you have Python installed on your system. Clone the repository and run `main.py`:

```bash
git clone https://github.com/your-username/astar-pathfinding.git
cd astar-pathfinding
python main.py
