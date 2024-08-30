class Cell:
    def __init__(self, position: tuple) -> None:
        self.position = position
        
    def changePosition(self, new_position) -> None:
        self.position = new_position
