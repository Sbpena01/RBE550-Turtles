import numpy as np
import matplotlib.pyplot as plt
import random

# Constants used throughout the script
SIZE = 128  # Size of the nxn board
COVERAGE = 1.0  # Percent of free space covered.

# Tetromino Pieces
PIECES = {
    "I" : [[0,0], [1,0], [2,0], [3,0]],
    "L" : [[0,0], [0,1], [1,1], [2,1]],
    "S" : [[0,0], [1,0], [1,1], [2,1]],
    "T" : [[0,0], [1,0], [1,1], [2,0]]
}

def rotatePiece(tetromino, rotation):
    """Performs a rotation on the provided tetromino

    Args:
        tetromino (_type_): The tetromino that will be rotated
        rotation (int): The angle (deg) to rotate the tetromino

    Returns:
        tetromino: The newly rotated tetromino
    """
    if rotation == 90:
        rotated_tetromino = [
            [tetromino[0][1], -tetromino[0][0]],
            [tetromino[1][1], -tetromino[1][0]],
            [tetromino[2][1], -tetromino[2][0]],
            [tetromino[3][1], -tetromino[3][0]]
        ]
    elif rotation == 180:
        rotated_tetromino = [
            [-tetromino[0][0], -tetromino[0][1]],
            [-tetromino[1][0], -tetromino[1][1]],
            [-tetromino[2][0], -tetromino[2][1]],
            [-tetromino[3][0], -tetromino[3][1]]
        ]
    elif rotation == 270:
        rotated_tetromino = [
            [-tetromino[0][1], tetromino[0][0]],
            [-tetromino[1][1], tetromino[1][0]],
            [-tetromino[2][1], tetromino[2][0]],
            [-tetromino[3][1], tetromino[3][0]]
        ]
    return tetromino
    

def placePiece(grid: np.ndarray, tetromino, origin: tuple):
    """Places a tetromino onto the grid to be displayed by plt.

    Args:
        grid (np.ndarray): The numpy matrix representing the obstacle field.
        tetromino (_type_): The tetromino to be placed in the grid.
        origin (tuple): The origin of the tetromino. Tetrominos are built with their
                          origins at their top left cell.
    """
    if len(origin) != 2:
        print("top_left must have 2 values to represent x and y coorindates")
    x = origin[0]
    y = origin[1]
    for arr in tetromino:
        new_x = max(0, min(x+arr[0], SIZE-1))
        new_y = max(0, min(y+arr[1], SIZE-1))
        grid[new_x][new_y] = 0

def calculateCoverage(coverage: float) -> int:
    """Calculates the number of pieces needed to reach a desired coverage.

    Args:
        coverage (float): Percent of the obstacle field to be covered by tetrominos

    Returns:
        int: The minimum number of tetrominos required to reach the desired coverage percent.
    """
    area = SIZE ** 2
    maximum_pieces = area / 4
    return int(maximum_pieces * coverage)

def checkForCollision(grid: np.ndarray, tetromino, origin: tuple):
    """Checks if the tetromino would collide/overlap with an existing tetromino on the grid.

    Args:
        grid (np.ndarray): The numpy matrix representing the obstacle field.
        tetromino (_type_): The tetromino that is being checked for collision.
        top_left (tuple): The origin of the tetromino

    Returns:
        _type_: _description_
    """
    x = origin[0]
    y = origin[1]
    for cell in tetromino:
        new_x = max(0, min(x+cell[0], SIZE-1))
        new_y = max(0, min(y+cell[1], SIZE-1))
        if grid[new_x][new_y] == 0:
            return True
    return False

def main():
    grid = np.ones((SIZE, SIZE))
    grid[100][10] = 0.0
    num_pieces = calculateCoverage(COVERAGE)
    print(num_pieces)
    for i in range(num_pieces):
        # We want to keep trying to place a piece until we can place the piece without
        # it overlapping an existing piece. Once the piece is placed, then the while loop
        # is broken. This does mean that any attempts at a field with >80% coverage will
        # likely take a long time, or be impossible. Hence, the second script.
        num_attempts = 0
        while True:
            x_coord = random.randint(0, SIZE)
            y_coord = random.randint(0, SIZE)
            piece = random.choice(list(PIECES.values()))
            rotation = random.choice(list([0, 90, 180, 270]))
            rotated_piece = rotatePiece(piece, rotation)
            if not checkForCollision(grid, rotated_piece, (x_coord, y_coord)) or num_attempts >= 20:
                num_attempts = 0
                placePiece(grid, rotated_piece, (x_coord, y_coord))
                # print("Successfully placed piece: ", i)
                break
            num_attempts += 1
    plt.imshow(grid, cmap="grey", interpolation=None)
    plt.title("Obstacle Field")
    plt.show()

if __name__ == "__main__":
    main()
