# import delay_tools as dl
import unittest
from delay_tools import delay_minutes as dm

# print(dm(35, 25))

class TestDelay(unittest.TestCase):

    def test_early(self):
        self.assertEqual(dm(25, 30), 0)
    def test_exact(self):
        self.assertEqual(dm(45, 45), 0)
    def test_later(self):
        self.assertEqual(dm(42, 30), 12)