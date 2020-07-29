import unittest
from recursion import factorial_sum, factorial, power

class TestRecursion(unittest.TestCase):

    def test_factorial(self):
        with self.assertRaisesRegex(Exception, "You need to factorial a number that is greater then 0"):
            factorial(0)
        with self.assertRaisesRegex(Exception, "You need to factorial a number that is greater then 0"):
            factorial(-2)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_sum(self):
        self.assertEqual(factorial_sum([0,0,0]), 0)
        self.assertEqual(factorial_sum([1, 1, 1]), 3)
        self.assertEqual(factorial_sum([1, 1, 22,23]), 47)
        self.assertEqual(factorial_sum([1, 1, 1, 3, -3]), 3)
        self.assertEqual(factorial_sum([-1, -1, -1]), -3)

    def test_power(self):
        with self.assertRaisesRegex(Exception, "You need to provide numbers that are greater then 0"):
            power(3, 0)
        with self.assertRaisesRegex(Exception, "You need to provide numbers that are greater then 0"):
            power(-1, 5)
        self.assertEqual(power(1,1), 1)
        self.assertEqual(power(2,2), 4)
        self.assertEqual(power(5,3), 125)
        self.assertEqual(power(3,4), 81)


