"""Math utility functions for logic checking and number properties.

This module contains clean, bug-free implementations of various mathematical properties
and algorithms, replacing calclass.txt and workpython.txt.
"""

import math
from typing import List, Optional


def is_prime(n: int) -> bool:
    """Check if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def is_pronic(n: int) -> bool:
    """Check if a number is a pronic (oblong) number.
    
    A pronic number is a number which is the product of two consecutive integers:
    n = x * (x + 1).
    """
    if n < 0:
        return False
    # If x*(x+1) = n, then x^2 + x - n = 0.
    # We can approximate x as sqrt(n).
    x = int(math.isqrt(n))
    return x * (x + 1) == n


def cube(a: float) -> float:
    """Calculate the cube of a number."""
    return a ** 3


def square(a: float) -> float:
    """Calculate the square of a number."""
    return a ** 2


def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong (narcissistic) number.
    
    An Armstrong number is a number that is the sum of its own digits each raised
    to the power of the number of digits.
    """
    if n < 0:
        return False
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n


def is_positive(a: float) -> bool:
    """Check if a number is positive (greater than or equal to 0)."""
    return a >= 0


def is_palindrome(n: int) -> bool:
    """Check if an integer is a palindrome (reads same forwards and backwards)."""
    if n < 0:
        return False
    num_str = str(n)
    return num_str == num_str[::-1]


def factorial(n: int) -> Optional[int]:
    """Calculate the factorial of a non-negative integer.
    
    Returns None if n is negative.
    """
    if n < 0:
        return None
    return math.factorial(n)


def is_strong(n: int) -> bool:
    """Check if a number is a Strong number (special number).
    
    A Strong number is a number where the sum of the factorials of its digits
    is equal to the number itself.
    """
    if n < 0:
        return False
    num_str = str(n)
    digit_factorials = []
    for digit in num_str:
        f = factorial(int(digit))
        if f is None:
            return False
        digit_factorials.append(f)
    return sum(digit_factorials) == n


def factors(n: int) -> List[int]:
    """Get all positive factors (divisors) of an integer n.
    
    Returns an empty list for n <= 0.
    """
    if n <= 0:
        return []
    result = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(list(result))


def is_harshad(n: int) -> bool:
    """Check if a number is a Harshad (Niven) number.
    
    A Harshad number is an integer that is divisible by the sum of its digits.
    """
    if n <= 0:
        return False
    digit_sum = sum(int(digit) for digit in str(n))
    if digit_sum == 0:
        return False
    return n % digit_sum == 0


def is_neon(n: int) -> bool:
    """Check if a number is a Neon number.
    
    A Neon number is a number where the sum of digits of its square
    is equal to the number itself.
    """
    sq = n * n
    digit_sum = sum(int(digit) for digit in str(sq))
    return digit_sum == n


def is_magic(n: int) -> bool:
    """Check if a number is a Magic number.
    
    A Magic number is a number where the recursive sum of its digits
    eventually equals 1.
    """
    if n <= 0:
        return False
    
    temp = n
    while temp >= 10:
        temp = sum(int(digit) for digit in str(temp))
    return temp == 1


def is_evil(n: int) -> bool:
    """Check if a number is an Evil number.
    
    An Evil number is a non-negative integer that has an even number of 1s
    in its binary expansion.
    """
    if n < 0:
        return False
    binary_str = bin(n)
    count_ones = binary_str.count('1')
    return count_ones % 2 == 0


def power(base: float, exponent: float) -> float:
    """Safely calculate base raised to the power of exponent."""
    return base ** exponent


def is_disarium(n: int) -> bool:
    """Check if a number is a Disarium number.
    
    A Disarium number is a number where the sum of its digits powered to
    their respective positions (1-indexed) equals the number itself.
    """
    if n < 0:
        return False
    num_str = str(n)
    digit_sum = sum(int(digit) ** (i + 1) for i, digit in enumerate(num_str))
    return digit_sum == n


def is_perfect(n: int) -> bool:
    """Check if a number is a Perfect number.
    
    A Perfect number is a positive integer that is equal to the sum of its proper
    positive divisors (excluding the number itself).
    """
    if n <= 1:
        return False
    # Proper factors are all factors excluding n itself
    proper_factors = factors(n)[:-1]
    return sum(proper_factors) == n
