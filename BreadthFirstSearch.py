from ObstacleField import ObstacleField as OF

class BreadthFirstSearch:
    def __init__(self, field: OF, start: tuple, goal: tuple) -> None:
        self.field = field
        self.start = field.getCell(start)
        self.goal = field.getCell(goal)
        self.queue = list()  # Append to add to end, pop() to take away from end
        
        
    
    def performSearch(self) -> list:
        """Generates a path from start to goal using Depth First Search Algorithm

        Returns:
            list: Final path from start to goal. If path is unsuccessful, then returned list
                  will be empty.
        """
        
        # Since this is a demo for homework, we want to make sure that the start and goal
        # cells are always free. If the goal is not a free cell and is an obstacle, then
        # the search algorithm will never find a solution, regardless of its quality
        self.start.setValue(0)
        self.goal.setValue(0)
        
        self.start.markVisited()
        self.queue.append(self.start)
        while self.queue:
            current_cell = self.queue.pop(0)
            if current_cell.getCoordinate() == self.goal.getCoordinate():
                return self.generatePath()
            neighbors = self.field.checkFourNeighbors(current_cell)
            for cell in neighbors:
                if not cell.isVisited():
                    cell.markVisited()
                    cell.setPrevious(current_cell)
                    cell.setValue(0.3)
                    self.queue.append(cell)
        return list()
    
    def generatePath(self) -> list:
        path = list()
        current_cell = self.goal
        while current_cell.getPrevious() is not None:
            current_cell.setValue(0.6)
            path.append(current_cell)
            current_cell = current_cell.getPrevious()
        return path
