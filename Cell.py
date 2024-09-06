class Cell():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.value = 0
    
    def getValue(self) -> float:
        return self.value
    
    def setValue(self, value) -> None:
        self.value = value
