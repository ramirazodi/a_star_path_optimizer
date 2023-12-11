import tkinter as tk
from grid_setup import create_grid
from astar_algorithm import astar
from visualization import draw_path

class PathfindingGUI:
    def __init__(self, root, rows, cols):
        self.root = root
        self.grid = create_grid(rows, cols)
        self.rows = rows
        self.cols = cols
        self.cell_width = 10
        self.start = None
        self.end = None
        self.visualize = False

        self.canvas = tk.Canvas(root, width=cols*self.cell_width, height=rows*self.cell_width)
        self.canvas.pack()
        self.draw_grid()

        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)

        self.visualize_button = tk.Button(root, text="Toggle Visualization",
                                          command=self.toggle_visualization)
        self.visualize_button.pack()

        self.start_button = tk.Button(root, text="Start Pathfinding",
                                      command=self.start_pathfinding)
        self.start_button.pack()

        self.clear_button = tk.Button(root, text="Clear Grid",
                                      command=self.clear_grid)
        self.clear_button.pack()

    def draw_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * self.cell_width
                y1 = i * self.cell_width
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_width
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="light grey", outline="black")

    def on_left_click(self, event):
        x, y = event.x // self.cell_width, event.y // self.cell_width
        if 0 <= x < self.cols and 0 <= y < self.rows:
            if not self.start:
                self.start = (x, y)
                self.canvas.create_rectangle(x*self.cell_width, y*self.cell_width,
                                             x*self.cell_width + 10, y*self.cell_width + 10,
                                             fill="green", outline="green")
            elif not self.end:
                self.end = (x, y)
                self.canvas.create_rectangle(x*self.cell_width, y*self.cell_width,
                                             x*self.cell_width + 10, y*self.cell_width + 10,
                                             fill="red", outline="red")

    def on_drag(self, event):
        x, y = event.x // self.cell_width, event.y // self.cell_width
        if 0 <= x < self.cols and 0 <= y < self.rows:
            if self.start != (x, y) and self.end != (x, y):
                self.grid[y][x] = 1
                self.canvas.create_rectangle(x*self.cell_width, y*self.cell_width,
                                             x*self.cell_width + 10, y*self.cell_width + 10,
                                             fill="black", outline="black")

    def toggle_visualization(self):
        self.visualize = not self.visualize
        self.visualize_button\
            .config(text="Visualization On" if self.visualize else "Visualization Off")

    def start_pathfinding(self):
        if self.start and self.end:
            path = astar(self.grid, self.start, self.end, self.canvas, self.visualize)
            if not self.visualize:
                draw_path(self.canvas, path)

    def clear_grid(self):
        self.canvas.delete("all")
        self.grid = create_grid(self.rows, self.cols)
        self.start = None
        self.end = None
        self.draw_grid()

