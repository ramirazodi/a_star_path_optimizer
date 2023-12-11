import numpy as np

def create_grid(rows, cols):
    """
    Creates a grid represented as a 2D numpy array.
    :param rows: Number of rows in the grid.
    :param cols: Number of columns in the grid.
    :return: A 2D numpy array representing the grid.
    """
    return np.zeros((rows, cols), dtype=int)

