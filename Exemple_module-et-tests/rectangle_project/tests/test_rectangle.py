import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from geometry import Rectangle


def unittest() -> None:
    cases = [
        (Rectangle(5, 10), 50, 5, 10),
        (Rectangle(4, 3), 12, 4, 3),
        (Rectangle(2, 8), 16, 2, 8),
    ]

    for rect, expected_area, expected_width, expected_height in cases:
        assert rect.area() == expected_area, (
            f"Expected area {expected_area}, but got {rect.area()}"
        )
        assert rect.width == expected_width, (
            f"Expected width {expected_width}, but got {rect.width}"
        )
        assert rect.height == expected_height, (
            f"Expected height {expected_height}, but got {rect.height}"
        )

    print("All tests passed !")


if __name__ == "__main__":
    unittest()