<p align="center">
  <img src="data/banner.svg" width="800" alt="Python Master Banner">
</p>

<p align="center">
  <img src="data/dashboard.svg" width="800" alt="Python Master Dashboard">
</p>

# 🐍 Python Master: Interactive Logic, Games & Analytics Suite

[![Python Version](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue?logo=python&logoColor=white)](https://python.org)
[![Tests Status](https://img.shields.io/badge/Tests-29%20Passed-brightgreen?logo=github-actions&logoColor=white)](https://github.com)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-green)](https://peps.python.org/pep-0008/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A beautifully refactored Python repository specializing in custom algorithms, interactive terminal mini-games, mathematical checkers, string processors, and similarity engines.

---

## 🎭 Terminal Hero Preview

```
+==========================================================+
|                         PYTHON                           |
|         🐍 Interactive Logic & Games Suite 🐍            |
+==========================================================+
 
 [ 🎮 Interactive Mini-Games ]
   1. Rock Paper Scissors (Human/Computer Simulation)
   2. Snakes & Ladders (Board Game)
   3. Russian Roulette (Elimination Survival)
 
 [ 🛠️ Command-Line Utilities ]
   4. City Name Fuzzy Matcher (difflib/fuzzywuzzy)
   5. Webseries Recommender (Euclidean Similarity engine)
   6. Geometry Area & Perimeter Calculator
   7. Interest Rate & Maturity Value Calculator
   8. Twin Palindrome Checker (Even/Odd index parsing)
   9. Character Case Converter
  10. Character & String Analyzer
 
 [ 📊 Diagnostics ]
  11. Run Automated Diagnostic Unit Tests
 
   0. Exit
============================================================
Enter your choice (0-11): 
```

---

## 📂 Project Architecture

The codebase has been restructured from a flat, redundant set of buggy `.txt` snippets into a modular, clean, package-based Python environment:

```
python-master/
├── .gitignore
├── requirements.txt
├── LICENSE
├── README.md
├── main.py                     # Unified interactive console dashboard
├── data/                       # Datasets & resource files
│   ├── cities_data.txt         # Fuzzy-search city corpus
│   ├── webseries.json          # Structured movie & ratings dataset
│   ├── banner.svg              # Title banner graphic
│   └── dashboard.svg           # Tech status developer card
├── games/                      # Refactored terminal mini-games
│   ├── __init__.py
│   ├── rock_paper_scissors.py  # Bug-free Rock Paper Scissors
│   ├── snakes_and_ladders.py   # Refactored Snakes & Ladders
│   └── russian_roulette.py     # Clean Russian Roulette
├── utils/                      # Core utility packages
│   ├── __init__.py
│   ├── math_utils.py           # Fixed math operations
│   ├── string_utils.py         # Fixed string operations
│   └── list_utils.py           # Fixed list operations & sorting
├── cli_apps/                   # Command-line utility scripts
│   ├── __init__.py
│   ├── fuzzy_match.py          # Fixed city fuzzy search
│   ├── movie_recommender.py    # Completed movie similarity recommender
│   ├── geometry.py             # Fixed area/perimeter calculator
│   ├── interest_calculator.py  # Fixed simple interest
│   ├── palindrome_checker.py   # Twin/even/odd palindrome checker
│   ├── case_converter.py       # Safe character case converter
│   └── character_analyzer.py   # Safe character analyzer
└── tests/                      # Automated unit test suite
    ├── __init__.py
    ├── test_math_utils.py
    ├── test_string_utils.py
    └── test_list_utils.py
```

---

## 🛠️ Comprehensive Bug Audit & Resolution

During a deep audit of the repository, over 15 critical bugs, logic errors, and duplicate scripts were discovered and resolved:

| Component | Function/File | Original Bug / Symptom | Refactored Solution |
| :--- | :--- | :--- | :--- |
| **Math** | `isprime` | Returned `True` immediately on composite odd numbers (e.g. 9 was prime). | Corrected loop logic to evaluate all divisors before returning `True`. |
| **Math** | `ispronic` | Evaluated `a * (i + 1) == a` (always false except for `i=0`). | Searched for `i` up to $\sqrt{a}$ such that $i(i+1) = a$. |
| **Math** | `isfactorial` | Initialized accumulator to 0 (factorial always returned 0). | Initialized accumulator to 1 and corrected range limits. |
| **Math** | `isfactor` | `n % i == 0` had no effect; returned `i` immediately on loop 1. | Accumulates and returns a sorted list of all proper positive divisors. |
| **Math** | `isniven` | Division by zero crashed when testing $0$. | Added a safety check to return `False` when the sum of digits is zero. |
| **Math** | `ismagic` | Only summed digits once, violating the recursive sum property. | Recursively sums digits until a single digit remains, checking if it is 1. |
| **Math** | `isevil` | Converted to binary using base-10 modulo (`t % 10`) with base-2 division. | Uses clean Python native binary string parsing (`bin(n)`). |
| **Math** | `isdisarium` | Exited on first iteration; used changing remainder `t` as power. | Uses enumeration to compute sum of digits powered to their index. |
| **Math** | `isperfect` | Return statement inside loop exited on first iteration. | Proper factors accumulated and evaluated outside the loop. |
| **String** | `ispositive_str` | Returned status on the first character comparison. | Checks all consecutive characters and returns `True` only if sorted. |
| **String** | `islowercase` | Used strict `< 'z'` (skipped 'z'); mutated string with `int`. | Rewritten using clean ord/chr code conversions, returning strings. |
| **String** | `isreplace` | Mutation of immutable string elements (`lst[i] = b` crashed). | Resolved string immutability correctly by building a new string. |
| **String** | `isfind` | Reference to global `c`, and potential `IndexError` crashes. | Re-implemented manually using clean, safe slicing search logic. |
| **Games** | `rockpaper` | Case mismatches ("rock" vs "Rock") and static computer choice. | Lowercases inputs, checks against enum, and chooses dynamically. |
| **Games** | `ladder` / `snake` | hardcoded P1-P4 players, duplicate logic, indentation bugs. | Unified into a list-based player system supporting custom board sizes. |
| **Lists** | `sec_maxnum` | Returns `c` instead of middle value when `c < b < a`. | Uses `sorted([a, b, c])[1]` which works for all permutations. |
| **CLI** | `FUzzywuzzy` | Tried loading hardcoded drive `d:\\cities_data.txt` (crashed). | Loads file dynamically relative to repository root with fallback logic. |
| **CLI** | `moviedata` | Unfinished rating script calling `.add()` on dictionary (crashed). | Created a full movie similarity & recommendation engine using JSON data. |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Shweta-Mishra-ai/python.git
cd python
```

### 2. Set Up a Virtual Environment (Recommended)
Isolate your project dependencies by setting up a local virtual environment:

* **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt)**:
  ```cmd
  python -m venv venv
  .\venv\Scripts\activate.bat
  ```
* **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies (Optional)
The core functionalities of the dashboard, games, and tools run on Python's built-in standard library. However, if you want enhanced fuzzy matching performance, you can install the optional dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Interactive Dashboard
Launch the unified console panel to play games or run scripts:
```bash
python main.py
```

### 5. Run Diagnostic Unit Tests
Verify the integrity of all calculation models by executing the test runner:
```bash
python -m unittest discover -s tests
```
All core utilities are guarded by **29 diagnostic unit tests** to prevent regression.

---
*Developed with ❤️ and refactored to the highest quality standards by Shweta Mishra.*
