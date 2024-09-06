import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random

import Utils
from Cell import Cell

FREE = 0
OBSTACLE = 1

class ObstacleField:
    
    def __init__(self, size) -> None:
        self.size = size
        self.field = self.generateField(size)
    
    def generateField(self, size):
        return {(x, y): Cell(x,y) for x in range(size) for y in range(size)}
    
    def getCell(self, coordinate):
        return self.field.get(coordinate)
    
    def placePiece(self, tetromino, origin) -> None:
        if len(origin) != 2:
            print("top_left must have 2 values to represent x and y coorindates")
        x = origin[0]
        y = origin[1]
        for cell in tetromino.shape:
            new_x = Utils.clamp(x+cell[0], 0, self.size-1)
            new_y = Utils.clamp(y+cell[1], 0, self.size-1)
            grid_cell = self.getCell((new_x, new_y))
            grid_cell.setValue(OBSTACLE)
    
    def checkForCollision(self, tetromino, origin) -> bool:
        x = origin[0]
        y = origin[1]
        for cell in tetromino.shape:
            new_x = Utils.clamp(x+cell[0], 0, self.size-1)
            new_y = Utils.clamp(y+cell[1], 0, self.size-1)
            grid_cell = self.getCell((new_x, new_y))
            if grid_cell.getValue() == OBSTACLE:
                return True
        return False
    
    def generateRandomPosition(self) -> tuple:
        x = random.randint(0, self.size)
        y = random.randint(0, self.size)
        return (x, y)
    
    def draw(self) -> None:
        grid = np.zeros((self.size, self.size))
        custom_color_map = colors.ListedColormap(['white', 'red', 'black'])
        for (x,y), cell in self.field.items():
            grid[x,y] = cell.getValue()
        plt.imshow(grid, cmap=custom_color_map, interpolation=None)
        plt.show()
