from ObstacleField import ObstacleField
from Tetromino import Tetromino
from Cell import Cell
from DepthFirstSearch import DepthFirstSearch as DFS

SIZE = 128
COVERAGE = 0.5

def main():
    area = SIZE ** 2
    maximum_pieces = area / 4
    num_pieces =  int(maximum_pieces * COVERAGE)
    field = ObstacleField(SIZE)
    
    start = (0,0)
    goal = (SIZE-1, SIZE-1)
    
    dfs = DFS(field, start, goal)
    
    for i in range(num_pieces):
        attempts = 0
        while attempts <= 20:
            new_piece = Tetromino.generateRandomShape()
            position = field.generateRandomPosition()
            if not field.checkForCollision(new_piece, position):
                field.placePiece(new_piece, position)
                break
            attempts += 1
    # field.setCell(start, 0)
    # field.setCell(goal, 0)
    
    dfs.generatePath()
    field.draw()

if __name__ == "__main__":
    main()
