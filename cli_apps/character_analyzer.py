"""Character Type Analyzer.

Refactors and improves charfind.txt.
Analyzes characters to classify them as uppercase, lowercase, numbers, or special keys.
Supports analyzing a single character or a full string.
"""

def classify_char(ch: str) -> str:
    """Classify a single character into lowercase, uppercase, digit, or special."""
    if len(ch) != 1:
        return "invalid length"
        
    if 'a' <= ch <= 'z':
        return "Lowercase Letter"
    elif 'A' <= ch <= 'Z':
        return "Uppercase Letter"
    elif '0' <= ch <= '9':
        return "Numeric Digit"
    elif ch.isspace():
        return "Whitespace Character"
    else:
        return "Special / Other Character"


def run_app() -> None:
    """Run the character analyzer application."""
    print("=" * 45)
    print("Character & String Analyzer".center(45))
    print("=" * 45)
    
    print("\nSelect Mode:")
    print("1. Analyze a Single Character")
    print("2. Analyze a full String")
    
    mode = input("Enter choice (1-2): ").strip()
    if mode == '1':
        ch = input("\nEnter character: ")
        if len(ch) == 0:
            print("Error: Empty input.")
            return
        # Analyze first character
        target = ch[0]
        classification = classify_char(target)
        print(f"\nCharacter '{target}' is classified as: {classification}")
        
    elif mode == '2':
        s = input("\nEnter string to analyze: ")
        if not s:
            print("Error: Empty input.")
            return
            
        print("\nAnalysis Results:")
        print(f"Original String: '{s}'")
        print("-" * 35)
        
        counts = {"lower": 0, "upper": 0, "digit": 0, "space": 0, "special": 0}
        for char in s:
            cls = classify_char(char)
            if "Lowercase" in cls:
                counts["lower"] += 1
            elif "Uppercase" in cls:
                counts["upper"] += 1
            elif "Numeric" in cls:
                counts["digit"] += 1
            elif "Whitespace" in cls:
                counts["space"] += 1
            else:
                counts["special"] += 1
                
        print(f" - Lowercase Letters: {counts['lower']}")
        print(f" - Uppercase Letters: {counts['upper']}")
        print(f" - Numeric Digits:    {counts['digit']}")
        print(f" - Whitespaces:       {counts['space']}")
        print(f" - Special Characters: {counts['special']}")
        print("-" * 35)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    run_app()
