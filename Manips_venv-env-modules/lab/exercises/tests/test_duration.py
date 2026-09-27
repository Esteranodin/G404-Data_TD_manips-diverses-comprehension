"""Extension starter: replace each explicit failing TODO with useful checks."""

import unittest

from exercises.duration_tools import minutes_to_hours


class DurationTests(unittest.TestCase):
    # en héritant de unittest.TestCase, ta classe DurationTests devient un ensemble de tests et de ses méthodes utiles
    def test_ninety_minutes(self):
        result = minutes_to_hours(90)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 1.5)

    def test_zero_and_fractional_minutes(self):
        self.assertIsInstance(minutes_to_hours(0), float)
        self.assertAlmostEqual(minutes_to_hours(0), 0.0)

        self.assertIsInstance(minutes_to_hours(0.5), float)
        self.assertAlmostEqual(minutes_to_hours(0.5), 1 / 120)

    def test_rejects_negative_and_nonfinite_values(self):
        for bad in (-1.0, float("inf"), float("nan")):
            with self.assertRaises(ValueError):
                minutes_to_hours(bad)

    def test_rejects_boolean_and_non_numeric_values(self):
        for bad in (True, "90", None, 90 + 0j):
            with self.assertRaises(TypeError):
                minutes_to_hours(bad)


if __name__ == "__main__":
    unittest.main()
