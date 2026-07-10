"""String utility functions for custom string processing.

This module contains clean, bug-free implementations of custom string algorithms,
replacing duplicate code in calclass.txt and str_work_fun.txt.
"""

def count_spaces(s: str) -> int:
    """Count the number of spaces in a string."""
    return s.count(' ')


def is_positive_str(s: str) -> bool:
    """Check if the characters of a string are in non-decreasing lexicographical order."""
    if len(s) <= 1:
        return True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


def is_palindrome(s: str) -> bool:
    """Check if a string reads the same forwards and backwards."""
    return s == s[::-1]


def to_lowercase(s: str) -> str:
    """Convert a string to lowercase manually using ASCII codes."""
    result = []
    for char in s:
        code = ord(char)
        if 65 <= code <= 90:  # 'A'-'Z'
            result.append(chr(code + 32))
        else:
            result.append(char)
    return "".join(result)


def to_uppercase(s: str) -> str:
    """Convert a string to uppercase manually using ASCII codes."""
    result = []
    for char in s:
        code = ord(char)
        if 97 <= code <= 122:  # 'a'-'z'
            result.append(chr(code - 32))
        else:
            result.append(char)
    return "".join(result)


def swap_case(s: str) -> str:
    """Swap the case of each character in a string manually using ASCII codes."""
    result = []
    for char in s:
        code = ord(char)
        if 65 <= code <= 90:  # Uppercase to Lowercase
            result.append(chr(code + 32))
        elif 97 <= code <= 122:  # Lowercase to Uppercase
            result.append(chr(code - 32))
        else:
            result.append(char)
    return "".join(result)


def to_titlecase(s: str) -> str:
    """Convert a string to title case manually using ASCII codes.
    
    Capitalizes the first character of each word and lowercases the rest.
    """
    if not s:
        return s
    result = []
    new_word = True
    for char in s:
        if char == ' ':
            result.append(char)
            new_word = True
        else:
            code = ord(char)
            if new_word:
                if 97 <= code <= 122:
                    result.append(chr(code - 32))
                else:
                    result.append(char)
                new_word = False
            else:
                if 65 <= code <= 90:
                    result.append(chr(code + 32))
                else:
                    result.append(char)
    return "".join(result)


def extract_substring(s: str, start: int, end: int) -> str:
    """Safely extract a slice of a string between start (inclusive) and end (exclusive)."""
    return s[start:end]


def find_substring(s: str, sub: str) -> int:
    """Search for a substring in a string.
    
    Returns the start index of the first occurrence, or -1 if not found.
    """
    n, m = len(s), len(sub)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        if s[i:i + m] == sub:
            return i
    return -1


def replace_char(s: str, target: str, replacement: str) -> str:
    """Replace all occurrences of a target substring with a replacement string."""
    # Since strings are immutable in Python, we construct a new string
    return s.replace(target, replacement)


def compare_strings(s1: str, s2: str) -> bool:
    """Compare two strings for exact equality."""
    return s1 == s2
