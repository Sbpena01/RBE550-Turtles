import numpy as np
import matplotlib.pyplot as plt
import random

## Coordinate Frame Note:
# X is down
# Y is right
# (0,0) is the top left corner

SIZE = 128
COVERAGE = 0.8  # Percent of free space covered.

# Tetromino Pieces
PIECES = {
    "I" : [[0,0], [1,0], [2,0], [3,0]],
    "L" : [[0,0], [0,1], [1,1], [2,1]],
    "S" : [[0,0], [1,0], [1,1], [2,1]],
    "T" : [[0,0], [1,0], [1,1], [2,0]]
}

def rotatePiece(tetromino, rotation):
    if rotation == 90:
        tetromino = [
            [tetromino[0][1], -tetromino[0][0]],
            [tetromino[1][1], -tetromino[1][0]],
            [tetromino[2][1], -tetromino[2][0]],
            [tetromino[3][1], -tetromino[3][0]]
        ]
    elif rotation == 180:
        tetromino = [
            [-tetromino[0][0], -tetromino[0][1]],
            [-tetromino[1][0], -tetromino[1][1]],
            [-tetromino[2][0], -tetromino[2][1]],
            [-tetromino[3][0], -tetromino[3][1]]
        ]
    elif rotation == 270:
        tetromino = [
            [-tetromino[0][1], tetromino[0][0]],
            [-tetromino[1][1], tetromino[1][0]],
            [-tetromino[2][1], tetromino[2][0]],
            [-tetromino[3][1], tetromino[3][0]]
        ]
    # print(tetromino)
    return tetromino
    

def placePiece(grid, tetromino, top_left: tuple):
    if len(top_left) != 2:
        print("top_left must have 2 values to represent x and y coorindates")
    x = top_left[0]
    y = top_left[1]
    for arr in tetromino:
        new_x = max(0, min(x+arr[0], SIZE-1))
        new_y = max(0, min(y+arr[1], SIZE-1))
        grid[new_x][new_y] = 0

def calculateCoverage(coverage) -> int:
    area = SIZE ** 2
    maximum_pieces = area / 4
    return int(maximum_pieces * coverage)

def checkForCollision(grid, piece, top_left: tuple):
    x = top_left[0]
    y = top_left[1]
    for cell in piece:
        new_x = max(0, min(x+cell[0], SIZE-1))
        new_y = max(0, min(y+cell[1], SIZE-1))
        if grid[new_x][new_y] == 0:
            return True
    return False

def main():
    grid = np.ones((SIZE, SIZE))
    grid[100][10] = 0.0
    num_pieces = calculateCoverage(COVERAGE)
    for i in range(num_pieces):
        while True:
            x_coord = random.randint(0, SIZE)
            y_coord = random.randint(0, SIZE)
            piece = random.choice(list(PIECES.values()))
            rotation = random.choice(list([0, 90, 180, 270]))
            rotated_piece = rotatePiece(piece, rotation)
            if not checkForCollision(grid, rotated_piece, (x_coord, y_coord)):
                placePiece(grid, rotated_piece, (x_coord, y_coord))
                print("Successfully placed piece: ", i)
                break
            print("Cannot place piece: ", i)
    plt.imshow(grid, cmap="grey", interpolation=None)
    plt.title("Obstacle Field")
    plt.show()

if __name__ == "__main__":
    main()
