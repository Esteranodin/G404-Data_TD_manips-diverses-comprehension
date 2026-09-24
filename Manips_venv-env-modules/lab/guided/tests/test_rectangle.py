"""Run from lab: python -m unittest discover -s guided/tests -v."""

import unittest

from guided.rectangle_tools import Rectangle, describe


class RectangleTests(unittest.TestCase):
    def test_area_is_numeric(self):
        result = Rectangle(4, 3).area()
        self.assertIsInstance(result, (int, float))
        self.assertNotIsInstance(result, bool)

    def test_area_values(self):
        for width, height, expected in ((4, 3, 12), (2.5, 4, 10), (0, 9, 0)):
            with self.subTest(width=width, height=height):
                self.assertEqual(Rectangle(width, height).area(), expected)

    def test_area_can_be_reused_in_a_calculation(self):
        self.assertEqual(Rectangle(4, 3).area() / 2, 6)

    def test_describe_returns_text(self):
        self.assertEqual(describe(Rectangle(4, 3)), "Area: 12")


if __name__ == "__main__":
    unittest.main()
