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
    
    def setCell(self, cell: tuple, value: int) -> None:
        self.field[cell[0], cell[1]] = value
    
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
        
    def isCellOutOfField(self, cell: tuple) -> bool:
        if cell[0] < 0 or cell[0] >= self.size:
            return True
        if cell[1] < 0 or cell[1] >= self.size:
            return True
        return False
      
    def checkFourNeighbors(self, cell: tuple) -> list:
        possible_neighbors = [
            (cell[0] - 1, cell[1]),  # Top
            (cell[0] + 1, cell[1]),  # Bottom
            (cell[0], cell[1] - 1),  # Left
            (cell[0], cell[1] + 1),  # Right
        ]
        free_neighbors = list()
        for neighbor in possible_neighbors:
            if self.isCellOutOfField(neighbor):
                continue
            if self.field[neighbor[0], neighbor[1]] == 0:
                free_neighbors.append(neighbor)
        return free_neighbors
            
    
    def checkEightNeighbors(self, cell: tuple) -> list:
        pass
