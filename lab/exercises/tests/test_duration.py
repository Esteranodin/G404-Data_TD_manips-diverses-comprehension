"""Extension starter: replace each explicit failing TODO with useful checks."""

import unittest

from exercises.duration_tools import minutes_to_hours


class DurationTests(unittest.TestCase):
    def test_ninety_minutes(self):
        result = minutes_to_hours(90)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 1.5)

    def test_zero_and_fractional_minutes(self):
        # TODO: Cover 0 minutes and 0.5 minutes, including returned types.
        self.fail("TODO: tester zéro et une durée fractionnaire.")

    def test_rejects_negative_and_nonfinite_values(self):
        # TODO: Use assertRaises(ValueError) for negative, inf and nan.
        self.fail("TODO: tester les valeurs numériques hors contrat.")

    def test_rejects_boolean_and_non_numeric_values(self):
        # TODO: Use assertRaises(TypeError) for True, '90' and None.
        self.fail("TODO: tester les types hors contrat.")


if __name__ == "__main__":
    unittest.main()
