"""Geometry area and perimeter calculator.

Refactors and improves areapython.txt.
Provides an interactive shape menu so inputs are only required for the chosen shape.
Fixes the circle area labelling bug.
"""

import math


def calculate_circle() -> None:
    """Prompt for radius and display area & circumference."""
    try:
        r = float(input("\nEnter the radius of the circle: ").strip())
        if r < 0:
            print("Radius cannot be negative!")
            return
        area = math.pi * (r ** 2)
        circumference = 2 * math.pi * r
        print(f"Area of Circle: {round(area, 4)}")
        print(f"Circumference of Circle: {round(circumference, 4)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def calculate_square() -> None:
    """Prompt for side and display area & perimeter."""
    try:
        s = float(input("\nEnter the side length of the square: ").strip())
        if s < 0:
            print("Side length cannot be negative!")
            return
        area = s * s
        perimeter = 4 * s
        print(f"Area of Square: {round(area, 4)}")
        print(f"Perimeter of Square: {round(perimeter, 4)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def calculate_rectangle() -> None:
    """Prompt for length and width and display area & perimeter."""
    try:
        l = float(input("\nEnter the length of the rectangle: ").strip())
        w = float(input("Enter the width of the rectangle: ").strip())
        if l < 0 or w < 0:
            print("Dimensions cannot be negative!")
            return
        area = l * w
        perimeter = 2 * (l + w)
        print(f"Area of Rectangle: {round(area, 4)}")
        print(f"Perimeter of Rectangle: {round(perimeter, 4)}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def calculate_triangle() -> None:
    """Prompt for base and height to calculate area/perimeter."""
    try:
        b = float(input("\nEnter the base of the triangle: ").strip())
        h = float(input("Enter the height of the triangle: ").strip())
        if b < 0 or h < 0:
            print("Dimensions cannot be negative!")
            return
        area = 0.5 * b * h
        print(f"Area of Triangle: {round(area, 4)}")
        
        calc_peri = input("Would you like to calculate the perimeter too? (y/n): ").strip().lower()
        if calc_peri == 'y':
            s1 = float(input("Enter length of side 1: ").strip())
            s2 = float(input("Enter length of side 2: ").strip())
            s3 = float(input("Enter length of side 3 (base): ").strip())
            if s1 < 0 or s2 < 0 or s3 < 0:
                print("Sides cannot be negative!")
                return
            perimeter = s1 + s2 + s3
            print(f"Perimeter of Triangle: {round(perimeter, 4)}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def run_app() -> None:
    """Main execution loop for the Geometry App."""
    print("=" * 45)
    print("Geometry Area & Perimeter Tool".center(45))
    print("=" * 45)
    
    while True:
        print("\nSelect a shape:")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Triangle")
        print("5. Exit")
        
        choice = input("Enter option (1-5): ").strip()
        if choice == '1':
            calculate_circle()
        elif choice == '2':
            calculate_square()
        elif choice == '3':
            calculate_rectangle()
        elif choice == '4':
            calculate_triangle()
        elif choice == '5' or choice.lower() in ['exit', 'q']:
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    run_app()
