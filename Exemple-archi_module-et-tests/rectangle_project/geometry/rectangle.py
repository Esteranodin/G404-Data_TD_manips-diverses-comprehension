class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    def area(self) -> int | float:
        return self.width * self.height