"""Starter with one intentional return-type defect to investigate together."""


class Rectangle:
    """Store two finite, nonnegative dimensions supplied by the caller."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the numeric area; this starter violates that contract."""
        # return f"Area: {self.width * self.height:g}"
        # en corrigé (return type float et fonction pour print avec formatage :g)
        return self.width * self.height


def describe(rectangle: Rectangle) -> str:
    """Build the text representation; keep presentation outside area()."""
    return f"Area: {rectangle.area():g}"
