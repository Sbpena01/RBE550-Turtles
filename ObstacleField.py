import numpy as np
import matplotlib.pyplot as plt
import random
import Utils

class ObstacleField:
    def __init__(self, size) -> None:
        self.size = size
        self.field = np.zeros((size, size))
    
    def placePiece(self, tetromino, origin) -> None:
        if len(origin) != 2:
            print("top_left must have 2 values to represent x and y coorindates")
        x = origin[0]
        y = origin[1]
        for cell in tetromino.shape:
            new_x = Utils.clamp(x+cell[0], 0, self.size-1)
            new_y = Utils.clamp(y+cell[1], 0, self.size-1)
            self.field[new_x][new_y] = 1
    
    def checkForCollision(self, tetromino, origin) -> bool:
        x = origin[0]
        y = origin[1]
        for cell in tetromino.shape:
            new_x = Utils.clamp(x+cell[0], 0, self.size-1)
            new_y = Utils.clamp(y+cell[1], 0, self.size-1)
            if self.field[new_x][new_y] == 1:
                return True
        return False
    
    def generateRandomPosition(self) -> tuple:
        x = random.randint(0, self.size)
        y = random.randint(0, self.size)
        return (x, y)
    
    def draw(self) -> None:
        plt.imshow(self.field, cmap="binary", interpolation=None)
        plt.show()
