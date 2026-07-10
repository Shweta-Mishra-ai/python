"""Unit tests for math_utils module."""

import unittest
from utils import math_utils


class TestMathUtils(unittest.TestCase):
    """Test cases for checking fixed mathematical utility functions."""

    def test_is_prime(self) -> None:
        self.assertFalse(math_utils.is_prime(-5))
        self.assertFalse(math_utils.is_prime(0))
        self.assertFalse(math_utils.is_prime(1))
        self.assertTrue(math_utils.is_prime(2))
        self.assertTrue(math_utils.is_prime(3))
        self.assertFalse(math_utils.is_prime(9))  # Fixed the original loop bug
        self.assertTrue(math_utils.is_prime(11))
        self.assertFalse(math_utils.is_prime(15))

    def test_is_pronic(self) -> None:
        self.assertTrue(math_utils.is_pronic(0))   # 0 * 1 = 0
        self.assertTrue(math_utils.is_pronic(2))   # 1 * 2 = 2
        self.assertTrue(math_utils.is_pronic(6))   # 2 * 3 = 6
        self.assertTrue(math_utils.is_pronic(12))  # 3 * 4 = 12
        self.assertTrue(math_utils.is_pronic(20))  # 4 * 5 = 20
        self.assertFalse(math_utils.is_pronic(3))
        self.assertFalse(math_utils.is_pronic(5))
        self.assertFalse(math_utils.is_pronic(-6))

    def test_is_armstrong(self) -> None:
        self.assertTrue(math_utils.is_armstrong(153))  # 1^3 + 5^3 + 3^3 = 153
        self.assertTrue(math_utils.is_armstrong(370))
        self.assertTrue(math_utils.is_armstrong(1634)) # 1^4 + 6^4 + 3^4 + 4^4 = 1634
        self.assertFalse(math_utils.is_armstrong(154))
        self.assertFalse(math_utils.is_armstrong(-153))

    def test_is_palindrome(self) -> None:
        self.assertTrue(math_utils.is_palindrome(121))
        self.assertTrue(math_utils.is_palindrome(0))
        self.assertTrue(math_utils.is_palindrome(1331))
        self.assertFalse(math_utils.is_palindrome(123))
        self.assertFalse(math_utils.is_palindrome(-121))

    def test_factorial(self) -> None:
        self.assertEqual(math_utils.factorial(0), 1)
        self.assertEqual(math_utils.factorial(1), 1)
        self.assertEqual(math_utils.factorial(5), 120)
        self.assertIsNone(math_utils.factorial(-1))

    def test_is_strong(self) -> None:
        # Sum of factorials of digits
        self.assertTrue(math_utils.is_strong(145))  # 1! + 4! + 5! = 1 + 24 + 120 = 145
        self.assertTrue(math_utils.is_strong(1))
        self.assertTrue(math_utils.is_strong(2))
        self.assertFalse(math_utils.is_strong(100))

    def test_factors(self) -> None:
        self.assertEqual(math_utils.factors(6), [1, 2, 3, 6])
        self.assertEqual(math_utils.factors(1), [1])
        self.assertEqual(math_utils.factors(0), [])
        self.assertEqual(math_utils.factors(-10), [])

    def test_is_harshad(self) -> None:
        self.assertTrue(math_utils.is_harshad(18))  # 18 is divisible by 9 (1+8)
        self.assertTrue(math_utils.is_harshad(20))  # 20 is divisible by 2 (2+0)
        self.assertFalse(math_utils.is_harshad(19)) # 19 is not divisible by 10 (1+9)
        self.assertFalse(math_utils.is_harshad(0))  # Safely handles 0 (does not divide by zero)

    def test_is_neon(self) -> None:
        self.assertTrue(math_utils.is_neon(9))  # 9^2 = 81 -> 8+1 = 9
        self.assertTrue(math_utils.is_neon(1))  # 1^2 = 1 -> 1
        self.assertFalse(math_utils.is_neon(5))

    def test_is_magic(self) -> None:
        self.assertTrue(math_utils.is_magic(19))   # 1+9=10 -> 1+0=1
        self.assertTrue(math_utils.is_magic(1729)) # 1+7+2+9=19 -> 1+9=10 -> 1+0=1
        self.assertFalse(math_utils.is_magic(22))  # 2+2=4

    def test_is_evil(self) -> None:
        self.assertTrue(math_utils.is_evil(3))   # bin(3) = 11 (two 1s -> even)
        self.assertTrue(math_utils.is_evil(5))   # bin(5) = 101 (two 1s -> even)
        self.assertFalse(math_utils.is_evil(7))  # bin(7) = 111 (three 1s -> odd)

    def test_is_disarium(self) -> None:
        self.assertTrue(math_utils.is_disarium(89))  # 8^1 + 9^2 = 8 + 81 = 89
        self.assertTrue(math_utils.is_disarium(175)) # 1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175
        self.assertFalse(math_utils.is_disarium(100))

    def test_is_perfect(self) -> None:
        self.assertTrue(math_utils.is_perfect(6))   # 1 + 2 + 3 = 6
        self.assertTrue(math_utils.is_perfect(28))  # 1 + 2 + 4 + 7 + 14 = 28
        self.assertFalse(math_utils.is_perfect(12)) # 1+2+3+4+6 = 16 != 12


if __name__ == "__main__":
    unittest.main()
