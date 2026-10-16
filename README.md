# Python Mini Challenges — Week 1 Internship Task 3

> **WeIntern Pvt. Ltd. Python Development Internship — Week 1 Assignment**

---

## 1. Project Objective

The primary objective of this project is to strengthen foundational problem-solving skills and demonstrate proficiency in core Python programming concepts. Through a modular and clean architecture, this repository implements 15 practical programming challenges categorized across:

- **Strings & String Manipulation**: Slicing, case transformations, character counting, and tokenization.
- **Lists & Sequence Operations**: Iteration, duplicates filtering, sorting algorithms, and element intersections.
- **Dictionaries & Key-Value Data Structures**: Frequency mappings, dictionary merging, validation, aggregation, and grouping.
- **Defensive Programming & Testing**: Modular separation of concerns, robust input parsing, exception handling, and 100% test coverage using Python's built-in `unittest` framework.

---

## 2. Technologies Used

- **Language**: Python 3.13+ (compatible with Python 3.10+)
- **Standard Library**: Built-in modules only (`sys`, `string`, `typing`, `unittest`, `pathlib`)
- **Testing Framework**: Python `unittest`
- **Version Control**: Git & GitHub

---

## 3. Project Structure

```text
python_mini_challenges/
│
├── main.py                  # Interactive console application with submenus
├── strings.py               # 5 string manipulation challenge functions
├── lists.py                 # 5 list operation challenge functions
├── dictionaries.py          # 5 dictionary & key-value challenge functions
├── README.md                # Project documentation and submission guide
├── .gitignore               # Excludes bytecode, caches, and virtual envs
│
└── tests/                   # Automated unittest test suite
    ├── __init__.py          # Test package marker
    ├── test_strings.py      # Unit tests for strings module
    ├── test_lists.py        # Unit tests for lists module
    └── test_dictionaries.py # Unit tests for dictionaries module
```

### Module Responsibilities

| File | Purpose |
| :--- | :--- |
| `strings.py` | Contains pure, reusable string manipulation functions independent of terminal I/O. |
| `lists.py` | Contains pure sequence and list manipulation functions including Bubble Sort. |
| `dictionaries.py` | Contains key-value aggregation, merging, and average calculation functions. |
| `main.py` | Command-line interface providing interactive submenus, input validation, and user feedback. |
| `tests/` | Comprehensive unit tests verifying standard inputs, edge cases, type checks, and error conditions. |
| `README.md` | Complete explanation of logic, execution guide, and internship review notes. |

---

## 4. Challenge Catalog & Logic Explanation

### Category A: String Manipulation (`strings.py`)

#### Challenge 1: Reverse a String (`reverse_string`)
- **Objective**: Accept a string and return its reversed version.
- **Logic**: Uses Python's native slice syntax `text[::-1]`, which traverses the sequence from the final index back to the beginning with a step of `-1`. Gracefully handles empty strings by returning `""`.
- **Sample Input**: `"python"`
- **Sample Output**: `"nohtyp"`

#### Challenge 2: Count Vowels (`count_vowels`)
- **Objective**: Count occurrences of vowels (`a`, `e`, `i`, `o`, `u`) in a case-insensitive manner.
- **Logic**: Converts the input string to lowercase and iterates through each character, checking membership in a pre-defined set of vowels `{'a', 'e', 'i', 'o', 'u'}`.
- **Sample Input**: `"Python Internship"`
- **Sample Output**: `4`

#### Challenge 3: Check Palindrome (`is_palindrome`)
- **Objective**: Determine whether a string reads identically forwards and backwards.
- **Logic**: Normalizes the string by filtering alphanumeric characters with `char.isalnum()` and converting them to lowercase. Then checks if `cleaned == cleaned[::-1]`. Whitespace and punctuation are ignored.
- **Sample Input**: `"Madam"` / `"race car"`
- **Sample Output**: `True` (Palindrome)

#### Challenge 4: Convert Sentence to Sentence Case (`to_sentence_case`)
- **Objective**: Format a sentence such that only the first character is capitalized and the remainder is lowercase.
- **Logic**: Strips leading and trailing whitespace, extracts the first character to uppercase via `.upper()`, and appends the lowercase remainder via `.lower()`.
- **Sample Input**: `"hELLO wORLD"`
- **Sample Output**: `"Hello world"`

#### Challenge 5: Word Frequency Counter (`count_word_frequency`)
- **Objective**: Count the frequency of each unique word in a sentence.
- **Logic**: Replaces punctuation symbols with spaces using `string.punctuation`, converts the text to lowercase, splits into words on whitespace, and tallies frequencies in a dictionary.
- **Sample Input**: `"Python is great, python is fun!"`
- **Sample Output**: `{'python': 2, 'is': 2, 'great': 1, 'fun': 1}`

---

### Category B: List Operations (`lists.py`)

#### Challenge 1: Find Largest and Smallest Numbers (`find_largest_and_smallest`)
- **Objective**: Determine the maximum and minimum values in a list of numbers.
- **Logic**: Performs a single O(n) pass over the list. Initializes both candidate values to `numbers[0]` and updates them whenever an element is strictly greater or smaller. Returns `(None, None)` for empty lists.
- **Sample Input**: `[4, 7, 2, 9, 5]`
- **Sample Output**: `Largest = 9, Smallest = 2`

#### Challenge 2: Remove Duplicates (`remove_duplicates`)
- **Objective**: Remove duplicate items while preserving the first-occurrence order.
- **Logic**: Maintains an auxiliary `seen` set for O(1) membership lookups and an `unique_items` list. Elements are appended to the list only if not already recorded in `seen`.
- **Sample Input**: `[4, 7, 2, 7, 9, 2]`
- **Sample Output**: `[4, 7, 2, 9]`

#### Challenge 3: Count Even and Odd Numbers (`count_even_odd`)
- **Objective**: Count even and odd integers in a list.
- **Logic**: Iterates through each integer and tests divisibility using `num % 2 == 0`. Updates `'even'` and `'odd'` counters inside a results dictionary.
- **Sample Input**: `[1, 2, 3, 4, 6]`
- **Sample Output**: `{'even': 3, 'odd': 2}`

#### Challenge 4: Sort a List with Bubble Sort (`bubble_sort`)
- **Objective**: Sort numeric values in ascending order without using `sort()` or `sorted()`.
- **Logic**: Creates a copy of the list. Compares adjacent elements `list[j]` and `list[j+1]`, swapping them if `list[j] > list[j+1]`. An early-exit flag `swapped` terminates the loop early if no swaps take place during an iteration.
- **Sample Input**: `[64, 34, 25, 12, 22, 11, 90]`
- **Sample Output**: `[11, 12, 22, 25, 34, 64, 90]`

#### Challenge 5: Find Common Elements (`find_common_elements`)
- **Objective**: Find distinct common elements between two lists without duplicating results.
- **Logic**: Converts the second list into a set for fast lookup. Iterates over the first list, appending elements to the output list if they exist in the set and have not been added yet.
- **Sample Input**: `List 1: [1, 2, 2, 3, 4]`, `List 2: [2, 3, 5]`
- **Sample Output**: `[2, 3]`

---

### Category C: Dictionary Problems (`dictionaries.py`)

#### Challenge 1: Character Frequency (`count_char_frequency`)
- **Objective**: Count the frequency of each character in a given string.
- **Logic**: Loops through the string character by character. If `ignore_spaces` is set to `True`, whitespace characters are skipped. Tally counts are tracked using a dictionary `frequency[char] = frequency.get(char, 0) + 1`.
- **Sample Input**: `"banana"`
- **Sample Output**: `{'b': 1, 'a': 3, 'n': 2}`

#### Challenge 2: Merge Two Dictionaries (`merge_dictionaries`)
- **Objective**: Merge two dictionaries into a new dictionary without mutating originals.
- **Duplicate Key Policy**: Keys in `dict2` take precedence and overwrite matching keys in `dict1`.
- **Logic**: Copies `dict1` via `dict(dict1)` and updates it with `dict2.items()`.
- **Sample Input**: `{'a': 1, 'b': 2}` and `{'b': 3, 'c': 4}`
- **Sample Output**: `{'a': 1, 'b': 3, 'c': 4}`

#### Challenge 3: Student Marks Average (`calculate_student_average`)
- **Objective**: Calculate the mean mark from a dictionary of student names and scores.
- **Logic**: Validates that all scores are non-negative numbers (int or float). Computes `sum(marks.values()) / len(marks)` and rounds to two decimal places. Returns `None` for an empty dictionary.
- **Sample Input**: `{'Ravi': 80, 'Neha': 90, 'Arjun': 70}`
- **Sample Output**: `Average Marks = 80.00`

#### Challenge 4: Find Key with Maximum Value (`find_key_with_max_value`)
- **Objective**: Identify the key associated with the highest value in a dictionary.
- **Logic**: Iterates over key-value pairs tracking the maximum value and its key. Returns `None` for empty dictionaries.
- **Sample Input**: `{'Math': 95, 'English': 88, 'Science': 92}`
- **Sample Output**: `'Math'`

#### Challenge 5: Group Values by Category (`group_by_category`)
- **Objective**: Group items under their corresponding category key.
- **Logic**: Accepts a list of `(item, category)` tuples or a `{item: category}` dictionary. Accumulates items into lists mapped by each category key: `{category: [item1, item2, ...]}`.
- **Sample Input**: `[('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit')]`
- **Sample Output**: `{'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}`

---

## 5. Execution Instructions

### Running the Interactive Console Application

1. Open your terminal or command prompt.
2. Navigate into the `python_mini_challenges` directory:
   ```bash
   cd python_mini_challenges
   ```
3. Run the main menu program:
   ```bash
   python main.py
   ```

### Menu Walkthrough
- Enter `1` for **String Challenges** submenu.
- Enter `2` for **List Challenges** submenu.
- Enter `3` for **Dictionary Challenges** submenu.
- Enter `4` to safely **Exit**.
- In every submenu, select any individual challenge (1–5) or choose `6` to return to the main menu.

---

## 6. Running Automated Tests

The project includes 62 unit test cases covering normal inputs, edge cases (empty strings, empty lists, empty dictionaries), repeated items, negative numbers, floats, and error validation.

Run all tests from the `python_mini_challenges` directory:
```bash
python -m unittest discover -s tests -v
```

### Expected Output
```text
Ran 62 tests in 0.007s

OK
```

---

## 7. Key Python Concepts Demonstrated

1. **Clean Code & PEP 8 Standards**:
   - Meaningful snake_case function and variable names.
   - Comprehensive docstrings with parameter descriptions, return types, and doctests.
   - Modular file organization keeping UI logic separate from domain functions.

2. **Sequence & Data Structure Mastery**:
   - String slicing (`[::-1]`), case normalization, and punctuation cleaning.
   - List filtering, ordering preservation with sets, and custom Bubble Sort implementation.
   - Dictionary tallying (`dict.get()`), dictionary comprehension, and key-value merges.

3. **Defensive Programming**:
   - Handling empty collections (`""`, `[]`, `{}`) safely without `IndexError` or `ZeroDivisionError`.
   - Explicit input validation and helpful, user-friendly error messages.

4. **Automated Testing**:
   - Test suites written using `unittest.TestCase`.
   - Testing positive, negative, edge-case, and exception branches.

---

## 8. GitHub Submission Instructions

To push this project to your Week 1 GitHub repository, execute the following commands in your terminal:

```bash
# 1. Navigate to your repository root (where python_mini_challenges is located)
cd "c:\Users\bhagya neela\OneDrive\Desktop\task 3"

# 2. Check Git status
git status

# 3. Stage the python_mini_challenges directory
git add python_mini_challenges

# 4. Commit changes with a descriptive message
git commit -m "Complete Python Mini Challenges"

# 5. Push to your Week 1 GitHub repository
git push origin main
```

> **Note**: If your default branch is `master`, use `git push origin master`.

---

## 9. Terminal Screenshot Verification Guide

To capture genuine terminal screenshots for your internship submission:
1. **Application Run Screenshot**:
   - Launch `python main.py`.
   - Run at least one challenge from Strings, Lists, and Dictionaries.
   - Take a clean screenshot showing both the input and formatted output.
2. **Automated Test Run Screenshot**:
   - Run `python -m unittest discover -s tests -v`.
   - Ensure the terminal displays the test list and the final `Ran 62 tests in ... OK`.
   - Capture the full terminal window.

---

## 10. Internship Checklist & Author Information

### Task 3 Requirements Checklist
- [x] **Category A (Strings)**: Minimum 3 challenges implemented (`reverse_string`, `count_vowels`, `is_palindrome`, plus `to_sentence_case`, `count_word_frequency`).
- [x] **Category B (Lists)**: Minimum 3 challenges implemented (`find_largest_and_smallest`, `remove_duplicates`, `count_even_odd`, plus `bubble_sort`, `find_common_elements`).
- [x] **Category C (Dictionaries)**: Minimum 3 challenges implemented (`count_char_frequency`, `merge_dictionaries`, `calculate_student_average`, plus `find_key_with_max_value`, `group_by_category`).
- [x] **Main Menu**: Interactive console with submenu navigation, input validation, and safe exit.
- [x] **Testing**: Automated `unittest` test suite with 62 passing test cases.
- [x] **Code Quality**: PEP 8 compliant, type hints, docstrings on every function, zero external dependencies.
- [x] **Documentation**: Complete, beginner-friendly `README.md`.

### Author Details
- **Intern Name**: Bhagya Neela
- **Internship Program**: Python Development Internship
- **Organization**: WeIntern Pvt. Ltd.
- **Assignment**: Week 1 — Task 3 (Python Mini Challenges)
- **Repository URL**: `https://github.com/YOUR-USERNAME/python-week1-assignment.git` *(Replace with your actual GitHub repository URL)*
