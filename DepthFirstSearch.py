from ObstacleField import ObstacleField as OF
from Node import Node

class DepthFirstSearch:
    def __init__(self, field: OF, start: tuple, goal: tuple) -> None:
        self.field = field
        self.start = start
        self.goal = goal
        self.stack = list()  # Append to add to end, pop() to take away from end
    
    def generatePath(self) -> list:
        """Generates a path from start to goal using Depth First Search Algorithm

        Returns:
            list: Final path from start to goal. If path is unsuccessful, then returned list
                  will be empty.
        """
        start = Node(self.start)
        start.markVisited()
        self.stack.append(start)
        while self.stack:
            current_cell = self.stack.pop()
            print(current_cell.getCoordinate())
            if current_cell.getCoordinate() == self.goal:
                # Return list to get to this cell.
                break
            neighbors = self.field.checkFourNeighbors(current_cell.getCoordinate())
        return list()
