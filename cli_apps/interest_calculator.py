"""Simple Interest & Maturity Value Calculator.

Refactors and improves sipy.txt.
Fixes output labelling ("maturity value is" instead of "interest is").
"""

def run_app() -> None:
    """Run the simple interest calculator."""
    print("=" * 45)
    print("Interest & Maturity Calculator".center(45))
    print("=" * 45)
    
    try:
        p = float(input("\nEnter the Principal Amount ($): ").strip())
        t = int(input("Enter the Time Period (Years): ").strip())
        
        if p < 0 or t < 0:
            print("Principal and Time cannot be negative!")
            return
            
        print("\nEnter Gender / Status:")
        print(" - 'f' for Female (Interest Rate: 7.7%)")
        print(" - 'm' for Male (Interest Rate: 7.0%)")
        print(" - 's' for Senior Citizen (Interest Rate: 8.5%)")
        g = input("Select option (f/m/s or press Enter for default 7%): ").strip().lower()
        
        if g == 'f':
            r = 7.7
            status = "Female"
        elif g == 'm':
            r = 7.0
            status = "Male"
        elif g == 's':
            r = 8.5
            status = "Senior Citizen"
        else:
            r = 7.0
            status = "Standard (Default)"
            
        si = (p * r * t) / 100
        mv = p + si
        
        print("\n" + "-" * 30)
        print(f"Applied Rate: {r}% ({status})")
        print(f"Simple Interest Accrued: ${round(si, 2)}")
        print(f"Total Maturity Value: ${round(mv, 2)}")
        print("-" * 30)
        
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


if __name__ == "__main__":
    run_app()
