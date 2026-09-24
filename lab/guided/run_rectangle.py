"""Observe the returned value and type before following the failing caller."""

from rectangle_tools import Rectangle, describe


def main() -> None:
    rectangle = Rectangle(4, 3)
    result = rectangle.area()
    print(f"repr(result) = {result!r}")
    print(f"type(result) = {type(result).__name__}")
    assert isinstance(result, (int, float)), "area() doit renvoyer un nombre."
    assert result == 12, "Le rectangle 4 × 3 doit avoir une aire de 12."
    print(describe(rectangle))


if __name__ == "__main__":
    main()
