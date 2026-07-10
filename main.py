"""Unified CLI Orchestrator for the Python Master Collection.

Provides a premium interactive terminal dashboard to run all games, CLI utilities,
and run automated diagnostic test suites.
"""

import sys
import unittest

def run_tests() -> None:
    """Discover and run all automated unit tests in the tests/ folder."""
    print("\n" + "=" * 50)
    print(" Running Automated Diagnostic Tests ".center(50, "*"))
    print("=" * 50)
    
    # Set up test runner
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    print(f"Tests Run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    if result.wasSuccessful():
        print(" SUCCESS: All checks passed! ".center(50, "🟢"))
    else:
        print(" FAILURE: Some checks failed! ".center(50, "🔴"))
    print("=" * 50)
    input("\nPress Enter to return to main menu...")


def run_fuzzy_match() -> None:
    from cli_apps import fuzzy_match
    fuzzy_match.run_app()
    input("\nPress Enter to return to main menu...")


def run_movie_recommender() -> None:
    from cli_apps import movie_recommender
    movie_recommender.run_app()
    input("\nPress Enter to return to main menu...")


def run_geometry() -> None:
    from cli_apps import geometry
    geometry.run_app()


def run_interest() -> None:
    from cli_apps import interest_calculator
    interest_calculator.run_app()
    input("\nPress Enter to return to main menu...")


def run_palindrome() -> None:
    from cli_apps import palindrome_checker
    palindrome_checker.run_app()
    input("\nPress Enter to return to main menu...")


def run_case_converter() -> None:
    from cli_apps import case_converter
    case_converter.run_app()
    input("\nPress Enter to return to main menu...")


def run_analyzer() -> None:
    from cli_apps import character_analyzer
    character_analyzer.run_app()
    input("\nPress Enter to return to main menu...")


def play_rps() -> None:
    from games import rock_paper_scissors
    rock_paper_scissors.play_game()


def play_snakes() -> None:
    from games import snakes_and_ladders
    snakes_and_ladders.play_game()


def play_roulette() -> None:
    from games import russian_roulette
    russian_roulette.run_roulette()


def print_banner() -> None:
    """Print a beautiful premium terminal header."""
    print("\033[94m" + "=" * 60)
    print("""
    ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
    ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
    ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
    ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
    ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
               🐍 Interactive Logic & Games Suite 🐍
    """ + "\033[0m")
    print("=" * 60)


def main() -> None:
    """Main interactive terminal loop."""
    while True:
        # Clear screen code for standard terminals
        print("\033[H\033[J", end="")
        print_banner()
        
        print("\n\033[95m[ 🎮 Interactive Mini-Games ]\033[0m")
        print("  1. Rock Paper Scissors (Human/Computer Simulation)")
        print("  2. Snakes & Ladders (Board Game)")
        print("  3. Russian Roulette (Elimination Survival)")
        
        print("\n\033[96m[ 🛠️ Command-Line Utilities ]\033[0m")
        print("  4. City Name Fuzzy Matcher (difflib/fuzzywuzzy)")
        print("  5. Webseries Recommender (Euclidean Similarity engine)")
        print("  6. Geometry Area & Perimeter Calculator")
        print("  7. Interest Rate & Maturity Value Calculator")
        print("  8. Twin Palindrome Checker (Even/Odd index parsing)")
        print("  9. Character Case Converter")
        print(" 10. Character & String Analyzer")
        
        print("\n\033[92m[ 📊 Diagnostics ]\033[0m")
        print(" 11. Run Automated Diagnostic Unit Tests")
        
        print("\n\033[91m  0. Exit\033[0m")
        print("=" * 60)
        
        choice = input("\nEnter your choice (0-11): ").strip()
        
        print("\033[H\033[J", end="")  # Clear screen before launching app
        
        if choice == '1':
            play_rps()
        elif choice == '2':
            play_snakes()
        elif choice == '3':
            play_roulette()
        elif choice == '4':
            run_fuzzy_match()
        elif choice == '5':
            run_movie_recommender()
        elif choice == '6':
            run_geometry()
        elif choice == '7':
            run_interest()
        elif choice == '8':
            run_palindrome()
        elif choice == '9':
            run_case_converter()
        elif choice == '10':
            run_analyzer()
        elif choice == '11':
            run_tests()
        elif choice == '0' or choice.lower() in ['exit', 'q']:
            print("\nGoodbye! Keep coding in Python. 🐍\n")
            sys.exit(0)
        else:
            input("Invalid selection. Press Enter to try again...")


if __name__ == "__main__":
    # Ensure standard color output in Windows terminal
    if sys.platform == "win32":
        import os
        os.system("color")
    main()
