from turtle import Turtle

TRIANGLE_ANGLE = 120
SIDE_LENGTH = 100

def createTurtleGraphics():
    t = Turtle()
    for i in range(0,3):
        t.forward(2 * SIDE_LENGTH)
        t.right(TRIANGLE_ANGLE)
        t.forward(SIDE_LENGTH)
        t.right(TRIANGLE_ANGLE)
    
    # Pause the script after the turtle is finished to prevent the screen from closing.
    input()

if __name__ == "__main__":
    createTurtleGraphics()
