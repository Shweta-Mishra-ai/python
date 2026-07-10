"""Unit tests for list_utils module."""

import unittest
from utils import list_utils


class TestListUtils(unittest.TestCase):
    """Test cases for checking custom list operation helper functions."""

    def test_sorted_insert(self) -> None:
        self.assertEqual(list_utils.sorted_insert([10, 20, 30, 50], 40), [10, 20, 30, 40, 50])
        self.assertEqual(list_utils.sorted_insert([], 5), [5])
        self.assertEqual(list_utils.sorted_insert([1, 2, 3], 0), [0, 1, 2, 3])
        self.assertEqual(list_utils.sorted_insert([1, 2, 3], 4), [1, 2, 3, 4])

    def test_pop_element(self) -> None:
        popped, remaining = list_utils.pop_element([10, 20, 30])
        self.assertEqual(popped, 30)
        self.assertEqual(remaining, [10, 20])
        
        with self.assertRaises(IndexError):
            list_utils.pop_element([])

    def test_delete_element(self) -> None:
        deleted, remaining = list_utils.delete_element([10, 20, 30, 40], 2)
        self.assertEqual(deleted, 30)
        self.assertEqual(remaining, [10, 20, 40])
        
        with self.assertRaises(IndexError):
            list_utils.delete_element([1, 2], 5)
        with self.assertRaises(IndexError):
            list_utils.delete_element([1, 2], -1)

    def test_min_max_normalize(self) -> None:
        self.assertEqual(list_utils.min_max_normalize([10, 20, 30]), [0.0, 0.5, 1.0])
        self.assertEqual(list_utils.min_max_normalize([5]), [0.0])
        self.assertEqual(list_utils.min_max_normalize([2, 2, 2]), [0.0, 0.0, 0.0])
        self.assertEqual(list_utils.min_max_normalize([]), [])

    def test_second_largest(self) -> None:
        # Test all permutations of three distinct values to verify the bug is fixed!
        self.assertEqual(list_utils.second_largest(1, 2, 3), 2)  # a < b < c
        self.assertEqual(list_utils.second_largest(1, 3, 2), 2)  # a < c < b
        self.assertEqual(list_utils.second_largest(2, 1, 3), 2)  # b < a < c
        self.assertEqual(list_utils.second_largest(2, 3, 1), 2)  # c < a < b (buggy permutation in original!)
        self.assertEqual(list_utils.second_largest(3, 1, 2), 2)  # b < c < a (buggy permutation in original!)
        self.assertEqual(list_utils.second_largest(3, 2, 1), 2)  # c < b < a
        
        # Test duplicates
        self.assertEqual(list_utils.second_largest(2, 2, 3), 2)
        self.assertEqual(list_utils.second_largest(1, 2, 2), 2)


if __name__ == "__main__":
    unittest.main()
