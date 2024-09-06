class Cell():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.value = 0
        self.visited = False
        self.previous = None
    
    def getValue(self) -> float:
        return self.value
    
    def setValue(self, value) -> None:
        self.value = value
        
    def markVisited(self) -> None:
        self.visited = True
        
    def isVisited(self) -> bool:
        return self.visited
        
    def getCoordinate(self) -> tuple:
        return (self.x, self.y)
    
    def setPrevious(self, cell) -> None:
        self.previous = cell
        
    def getPrevious(self):
        return self.previous
