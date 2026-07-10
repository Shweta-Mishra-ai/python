"""Twin Palindrome Checker.

Refactors and improves palindrome_family.txt.
Analyzes if even-indexed and odd-indexed substrings of a string are palindromes.
Uses string_utils.is_palindrome for checks.
"""

from utils.string_utils import is_palindrome


def check_palindrome_family(s: str) -> None:
    """Classify the string into the palindrome family."""
    if not s:
        print("Input cannot be empty.")
        return
        
    e_str = ""
    o_str = ""
    for i, char in enumerate(s):
        if i % 2 == 0:
            e_str += char
        else:
            o_str += char
            
    is_even_palindrome = is_palindrome(e_str)
    is_odd_palindrome = is_palindrome(o_str)
    
    print("\n" + "-" * 30)
    print(f"Original String: '{s}'")
    print(f"Even-indexed chars: '{e_str}' (Palindrome: {is_even_palindrome})")
    print(f"Odd-indexed chars: '{o_str}' (Palindrome: {is_odd_palindrome})")
    print("-" * 30)
    
    if is_even_palindrome and is_odd_palindrome:
        print("Classification: 🌟 TWIN PALINDROME 🌟")
    elif is_even_palindrome and not is_odd_palindrome:
        print("Classification: EVEN PALINDROME")
    elif not is_even_palindrome and is_odd_palindrome:
        print("Classification: ODD PALINDROME")
    else:
        print("Classification: NOT PALINDROME")
    print("-" * 30)


def run_app() -> None:
    """Run the Palindrome Family Checker app."""
    print("=" * 45)
    print("Twin Palindrome Analyzer".center(45))
    print("=" * 45)
    
    s = input("\nEnter string to analyze: ").strip()
    check_palindrome_family(s)


if __name__ == "__main__":
    run_app()
