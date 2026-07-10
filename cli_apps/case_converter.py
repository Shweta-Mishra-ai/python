"""Interactive Character Case Converter.

Refactors and improves upperlower.txt.
Safely converts characters between uppercase and lowercase with safety bounds checking.
"""

from utils.string_utils import to_uppercase, to_lowercase


def convert_char() -> None:
    """Run interactive character conversion."""
    print("\n[Uppercase Converter]")
    char_up = input("Enter a lowercase character: ").strip()
    if not char_up:
        print("Error: No character entered.")
    else:
        # Convert first character
        c = char_up[0]
        res = to_uppercase(c)
        print(f"Result: '{res}'")
        
    print("\n[Lowercase Converter]")
    char_low = input("Enter an uppercase character: ").strip()
    if not char_low:
        print("Error: No character entered.")
    else:
        # Convert first character
        c = char_low[0]
        res = to_lowercase(c)
        print(f"Result: '{res}'")


def run_app() -> None:
    """Run the case converter application."""
    print("=" * 45)
    print("Character Case Converter".center(45))
    print("=" * 45)
    convert_char()


if __name__ == "__main__":
    run_app()
