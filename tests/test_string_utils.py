"""Unit tests for string_utils module."""

import unittest
from utils import string_utils


class TestStringUtils(unittest.TestCase):
    """Test cases for checking custom string helper functions."""

    def test_count_spaces(self) -> None:
        self.assertEqual(string_utils.count_spaces("hello world"), 1)
        self.assertEqual(string_utils.count_spaces("   "), 3)
        self.assertEqual(string_utils.count_spaces("nospaces"), 0)

    def test_is_positive_str(self) -> None:
        self.assertTrue(string_utils.is_positive_str("abc"))
        self.assertTrue(string_utils.is_positive_str("aabbcc"))
        self.assertFalse(string_utils.is_positive_str("cba"))  # Fixed early return bug
        self.assertTrue(string_utils.is_positive_str("a"))
        self.assertTrue(string_utils.is_positive_str(""))

    def test_is_palindrome(self) -> None:
        self.assertTrue(string_utils.is_palindrome("racecar"))
        self.assertTrue(string_utils.is_palindrome("aba"))
        self.assertFalse(string_utils.is_palindrome("hello"))

    def test_to_lowercase(self) -> None:
        self.assertEqual(string_utils.to_lowercase("ABC"), "abc")
        self.assertEqual(string_utils.to_lowercase("AbC123!"), "abc123!")
        self.assertEqual(string_utils.to_lowercase("XYZ"), "xyz")  # checks 'Z' boundary

    def test_to_uppercase(self) -> None:
        self.assertEqual(string_utils.to_uppercase("abc"), "ABC")
        self.assertEqual(string_utils.to_uppercase("AbC123!"), "ABC123!")
        self.assertEqual(string_utils.to_uppercase("xyz"), "XYZ")  # checks 'z' boundary

    def test_swap_case(self) -> None:
        self.assertEqual(string_utils.swap_case("aBcDe"), "AbCdE")
        self.assertEqual(string_utils.swap_case("Hello World 123!"), "hELLO wORLD 123!")

    def test_to_titlecase(self) -> None:
        self.assertEqual(string_utils.to_titlecase("hello world"), "Hello World")
        self.assertEqual(string_utils.to_titlecase("HELLO WORLD"), "Hello World")
        self.assertEqual(string_utils.to_titlecase("a b c"), "A B C")

    def test_extract_substring(self) -> None:
        self.assertEqual(string_utils.extract_substring("hello", 1, 4), "ell")
        self.assertEqual(string_utils.extract_substring("hello", 0, 100), "hello")

    def test_find_substring(self) -> None:
        self.assertEqual(string_utils.find_substring("hello world", "world"), 6)
        self.assertEqual(string_utils.find_substring("hello world", "abc"), -1)
        self.assertEqual(string_utils.find_substring("hello", "o"), 4)

    def test_replace_char(self) -> None:
        # Check that target characters are correctly replaced without raising TypeError
        self.assertEqual(string_utils.replace_char("banana", "a", "o"), "bonono")
        self.assertEqual(string_utils.replace_char("banana", "xyz", "o"), "banana")

    def test_compare_strings(self) -> None:
        self.assertTrue(string_utils.compare_strings("test", "test"))
        self.assertFalse(string_utils.compare_strings("test", "Test"))


if __name__ == "__main__":
    unittest.main()
