from ObstacleField import ObstacleField as OF
from Cell import Cell

class DepthFirstSearch:
    def __init__(self, field: OF, start: tuple, goal: tuple) -> None:
        self.field = field
        self.start = field.getCell(start)
        self.goal = field.getCell(goal)
        self.stack = list()  # Append to add to end, pop() to take away from end
    
    def performSearch(self) -> list:
        """Generates a path from start to goal using Depth First Search Algorithm

        Returns:
            list: Final path from start to goal. If path is unsuccessful, then returned list
                  will be empty.
        """
        self.start.markVisited()
        self.stack.append(self.start)
        while self.stack:
            current_cell = self.stack.pop()
            if current_cell.getCoordinate() == self.goal.getCoordinate():
                return self.generatePath()
            neighbors = self.field.checkFourNeighbors(current_cell)
            for cell in neighbors:
                if not cell.isVisited():
                    cell.markVisited()
                    cell.setPrevious(current_cell)
                    cell.setValue(0.3)
                    self.stack.append(cell)
        return list()
    
    def generatePath(self) -> list:
        path = list()
        current_cell = self.goal
        while current_cell.getPrevious() is not None:
            current_cell.setValue(0.6)
            path.append(current_cell)
            current_cell = current_cell.getPrevious()
        return path
