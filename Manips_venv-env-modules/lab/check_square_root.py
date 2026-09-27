import math
import unittest


class SquareRootTests(unittest.TestCase):
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            math.sqrt(-1)

if __name__ == "__main__":
    unittest.main()