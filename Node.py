class Node:
    def __init__(self, coordinate: tuple) -> None:
        self.coordinate = coordinate
        self.visited = False
        self.previous = None
    
    def getCoordinate(self) -> tuple:
        return self.coordinate
    
    def markVisited(self) -> None:
        self.visited = True
    
    def isVisited(self) -> bool:
        return self.visited
    
    def setPrevious(self, node) -> None:
        self.previous = node
