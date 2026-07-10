"""City name fuzzy matching application.

Refactors FUzzywuzzy.txt and fuzz.txt.
Fixes local absolute path error to use a dynamic path pointing to data/cities_data.txt.
Includes a robust fallback to Python's standard library difflib in case fuzzywuzzy is not installed.
"""

import os
from typing import List

# Try importing fuzzywuzzy
try:
    from fuzzywuzzy import process
    HAS_FUZZYWUZZY = True
except ImportError:
    import difflib
    HAS_FUZZYWUZZY = False


def load_city_data() -> List[str]:
    """Load city data from the data directory.
    
    Uses dynamic path resolution to avoid hardcoding.
    """
    # Resolve path: current_file -> cli_apps/ -> python-master/ -> data/cities_data.txt
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "cities_data.txt")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"City data file not found at: {file_path}")
        
    with open(file_path, "r", encoding="utf-8") as f:
        # Split by lines and remove empty strings
        data = [line.strip() for line in f.read().split('\n') if line.strip()]
    return data


def run_app() -> None:
    """Main execution of the fuzzy matching app."""
    print("=" * 45)
    print("City Fuzzy Matcher".center(45))
    print("=" * 45)
    
    try:
        data = load_city_data()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please check that data/cities_data.txt exists.")
        return

    print(f"Loaded {len(data)} cities. Enter your city name below.")
    cname = input("Enter city: ").strip()
    if not cname:
        print("Input cannot be empty.")
        return

    if HAS_FUZZYWUZZY:
        # fuzzywuzzy returns list of tuples: (match, score)
        res = process.extract(cname, choices=data, limit=8)
        best_match, score = res[0]
        print(f"\n[Using fuzzywuzzy] Top matches for '{cname}':")
        if score == 100:
            print(f"Perfect Match found: {best_match} (Score: {score})")
        else:
            for match, match_score in res:
                print(f" - {match} (Score: {match_score})")
    else:
        # Standard library fallback
        print("\nNote: fuzzywuzzy is not installed. Falling back to standard 'difflib' matching.")
        print("Tip: Install fuzzywuzzy for better scores (pip install fuzzywuzzy python-Levenshtein).")
        
        # get_close_matches returns list of matches ordered by score
        matches = difflib.get_close_matches(cname, data, n=8, cutoff=0.3)
        if matches:
            print(f"Top matches for '{cname}':")
            for match in matches:
                # Calculate similarity score using SequenceMatcher
                score = round(difflib.SequenceMatcher(None, cname, match).ratio() * 100, 1)
                print(f" - {match} (Similarity: {score}%)")
        else:
            print(f"No close matches found for '{cname}'.")


if __name__ == "__main__":
    run_app()
