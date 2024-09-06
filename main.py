from ObstacleField import ObstacleField
from Tetromino import Tetromino
from Cell import Cell

SIZE = 128
COVERAGE = 0.5

def main():
    area = SIZE ** 2
    maximum_pieces = area / 4
    num_pieces =  int(maximum_pieces * COVERAGE)
    field = ObstacleField(SIZE)
    for i in range(num_pieces):
        attempts = 0
        while attempts <= 20:
            new_piece = Tetromino.generateRandomShape()
            position = field.generateRandomPosition()
            if not field.checkForCollision(new_piece, position):
                field.placePiece(new_piece, position)
                break
            attempts += 1
    field.draw()
    pass

if __name__ == "__main__":
    main()
