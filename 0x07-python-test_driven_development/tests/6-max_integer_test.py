import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-5, -3, -2, -1, -4]), -1)

        # Test with a list containing both positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing a single integer
        self.assertEqual(max_integer([10]), 10)

        # Test with a list containing repeated integers
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

if __name__ == "__main__":
    unittest.main()

