import random

class Tetromino:
    
    SHAPES = {
    "I" : [[0,0], [1,0], [2,0], [3,0]],
    "L" : [[0,0], [0,1], [1,1], [2,1]],
    "S" : [[0,0], [1,0], [1,1], [2,1]],
    "T" : [[0,0], [1,0], [1,1], [2,0]]
    }
    
    def __init__(self, shape: str) -> None:
        self.shape = self.SHAPES[shape]
        self.origin = (0,0)
    
    def generateRandomShape():
        shape = random.choice(list(Tetromino.SHAPES.keys()))
        return Tetromino(shape)
