"""List utility functions for custom list operations and normalization.

This module contains clean, bug-free implementations of manual list processing functions
and algorithms, replacing duplicate code in lst_ist.txt, lst_dis.txt, and sec_maxnum.txt.
"""

from typing import List, Tuple, Union

Num = Union[int, float]

def sorted_insert(lst: List[Num], num: Num) -> List[Num]:
    """Insert a number into a copy of a sorted list in the correct position.
    
    Returns the new sorted list.
    """
    new_lst = list(lst)
    for i, val in enumerate(new_lst):
        if num <= val:
            new_lst.insert(i, num)
            return new_lst
    new_lst.append(num)
    return new_lst


def pop_element(lst: List[Num]) -> Tuple[Num, List[Num]]:
    """Remove and return the last element from a list.
    
    Returns a tuple: (popped_element, remaining_list).
    Raises IndexError if the list is empty.
    """
    if not lst:
        raise IndexError("pop from empty list")
    return lst[-1], lst[:-1]


def delete_element(lst: List[Num], idx: int) -> Tuple[Num, List[Num]]:
    """Remove and return an element at a specific index from a list.
    
    Returns a tuple: (deleted_element, remaining_list).
    Raises IndexError if index is out of bounds.
    """
    if idx < 0 or idx >= len(lst):
        raise IndexError("list index out of range")
    deleted_val = lst[idx]
    remaining_lst = lst[:idx] + lst[idx + 1:]
    return deleted_val, remaining_lst


def min_max_normalize(lst: List[Num]) -> List[float]:
    """Normalize a list of numbers to the range [0, 1] using Min-Max scaling.
    
    If all elements are equal, returns a list of 0.0 values.
    """
    if not lst:
        return []
    s = max(lst)
    r = min(lst)
    if s == r:
        return [0.0] * len(lst)
    return [float(x - r) / float(s - r) for x in lst]


def second_largest(a: Num, b: Num, c: Num) -> Num:
    """Return the second largest (middle) value of three numbers.
    
    Fixes the comparison bugs in sec_maxnum.txt.
    """
    return sorted([a, b, c])[1]
