<p align="center">
  <img src="data/banner.svg" width="800" alt="Python Master Banner">
</p>

<p align="center">
  <img src="data/dashboard.svg" width="800" alt="Python Master Dashboard">
</p>

# 🐍 Python Master: Logic, Games & Utilities Suite

[![Tests](https://github.com/Shweta-Mishra-ai/python/actions/workflows/tests.yml/badge.svg)](https://github.com/Shweta-Mishra-ai/python/actions/workflows/tests.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Code Style: PEP 8](https://img.shields.io/badge/Code%20Style-PEP%208-green)](https://peps.python.org/pep-0008/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Shweta-Mishra-ai/python?style=social)](https://github.com/Shweta-Mishra-ai/python)

A collection of terminal mini-games, math/string utilities, and small CLI tools — rebuilt from my own early Python scripts into a clean, modular, unit-tested package.

> **What this repo is:** some of the first Python I ever wrote (~4 years ago), originally a flat set of buggy, redundant scripts. I went back and reorganized it into a proper package, fixed 18 documented bugs, and added a unit-test suite. It's a code-hygiene and refactoring exercise more than a product — kept public as a transparent record of that cleanup.

---

## 🎭 Terminal Preview

```
+==========================================================+
|                         PYTHON                           |
|            🐍 Logic & Games Suite 🐍                     |
+==========================================================+

 [ 🎮 Mini-Games ]
   1. Rock Paper Scissors (Human vs Computer)
   2. Snakes & Ladders (Board Game)
   3. Russian Roulette (Elimination)

 [ 🛠️ Command-Line Utilities ]
   4. City Name Fuzzy Matcher (difflib / fuzzywuzzy)
   5. Web-series Recommender (Euclidean similarity)
   6. Geometry Area & Perimeter Calculator
   7. Interest & Maturity Value Calculator
   8. Twin Palindrome Checker
   9. Character Case Converter
  10. Character & String Analyzer

 [ 📊 Diagnostics ]
  11. Run Unit Tests

   0. Exit
============================================================
Enter your choice (0-11):
```

---

## 📂 Project Structure

Restructured from flat, redundant `.txt` snippets into a modular, package-based layout:

```
python-master/
├── main.py                     # Unified interactive console dashboard
├── requirements.txt
├── LICENSE
├── README.md
├── data/                       # Datasets & resource files
│   ├── cities_data.txt         # Fuzzy-search city corpus
│   ├── webseries.json          # Movie & ratings dataset
│   ├── banner.svg
│   └── dashboard.svg
├── games/                      # Terminal mini-games
│   ├── rock_paper_scissors.py
│   ├── snakes_and_ladders.py
│   └── russian_roulette.py
├── utils/                      # Core utility packages
│   ├── math_utils.py
│   ├── string_utils.py
│   └── list_utils.py
├── cli_apps/                   # Command-line utility scripts
│   ├── fuzzy_match.py
│   ├── movie_recommender.py
│   ├── geometry.py
│   ├── interest_calculator.py
│   ├── palindrome_checker.py
│   ├── case_converter.py
│   └── character_analyzer.py
└── tests/                      # Unit test suite
    ├── test_math_utils.py
    ├── test_string_utils.py
    └── test_list_utils.py
```

---

## 🛠️ Bug Audit & Fixes

The main value of this repo is the cleanup itself. 18 bugs, logic errors, and broken scripts were found and fixed during the rewrite:

| Component | Function/File | Original Bug | Fix |
| :--- | :--- | :--- | :--- |
| Math | `isprime` | Returned `True` on composite odd numbers (9 read as prime). | Evaluates all divisors before returning `True`. |
| Math | `ispronic` | `a * (i + 1) == a` was always false except `i=0`. | Searches `i` up to √a such that `i(i+1) = a`. |
| Math | `isfactorial` | Accumulator started at 0, so factorial always returned 0. | Accumulator starts at 1; range limits corrected. |
| Math | `isfactor` | `n % i == 0` had no effect; returned on first loop. | Returns a sorted list of all proper divisors. |
| Math | `isniven` | Division by zero crashed on input 0. | Returns `False` when digit sum is zero. |
| Math | `ismagic` | Summed digits only once. | Recursively sums digits down to one, checks for 1. |
| Math | `isevil` | Base-10 modulo mixed with base-2 division. | Uses native `bin(n)` parsing. |
| Math | `isdisarium` | Exited on first iteration; wrong power source. | Uses enumeration for sum of digits^index. |
| Math | `isperfect` | `return` inside loop exited early. | Factors accumulated and checked after the loop. |
| String | `ispositive_str` | Returned on first character comparison. | Checks all characters; `True` only if sorted. |
| String | `islowercase` | Strict `< 'z'` skipped 'z'; mutated string with `int`. | Rewritten with clean ord/chr conversions. |
| String | `isreplace` | Mutating an immutable string crashed. | Builds a new string instead. |
| String | `isfind` | Global `c` reference and `IndexError` risk. | Reimplemented with safe slicing search. |
| Games | `rockpaper` | Case mismatch and static computer choice. | Lowercases input; computer chooses dynamically. |
| Games | `snake` / `ladder` | Hardcoded players, duplicate logic, indentation bugs. | Unified list-based players; custom board sizes. |
| Lists | `sec_maxnum` | Returned wrong value when `c < b < a`. | Uses `sorted([a, b, c])[1]`. |
| CLI | `fuzzy_match` | Loaded a hardcoded `d:\cities_data.txt` (crashed). | Loads relative to repo root with fallback. |
| CLI | `movie_recommender` | Unfinished script called `.add()` on a dict. | Full similarity/recommendation engine over JSON. |

---

## 🚀 Getting Started

**1. Clone**
```bash
git clone https://github.com/Shweta-Mishra-ai/python.git
cd python
```

**2. (Optional) Virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate
```

**3. (Optional) Dependencies**

Core features run on the standard library. For faster fuzzy matching:
```bash
pip install -r requirements.txt
```

**4. Run the dashboard**
```bash
python main.py
```

**5. Run the tests**
```bash
python -m unittest discover -s tests
```

---

## 📄 License

MIT — see [LICENSE](LICENSE).
