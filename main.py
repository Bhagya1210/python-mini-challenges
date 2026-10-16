"""Main Application Menu for Python Mini Challenges.

Week 1 Internship Task 3 - WeIntern Pvt. Ltd. Python Development Internship.

This module provides an interactive console-based menu system allowing users
to explore and execute challenges across three categories:
- Category A: String Manipulation
- Category B: List Operations
- Category C: Dictionary Problems
"""

import sys
from typing import Any

from strings import (
    count_vowels,
    count_word_frequency,
    is_palindrome,
    reverse_string,
    to_sentence_case,
)
from lists import (
    bubble_sort,
    count_even_odd,
    find_common_elements,
    find_largest_and_smallest,
    remove_duplicates,
)
from dictionaries import (
    calculate_student_average,
    count_char_frequency,
    find_key_with_max_value,
    group_by_category,
    merge_dictionaries,
)


def print_header(title: str) -> None:
    """Print a visually distinct header for menus and challenge outputs."""
    width = 54
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def prompt_text(message: str) -> str:
    """Prompt the user for a text string."""
    return input(f"{message}: ").strip()


def parse_numeric_list(prompt_message: str) -> list[float] | None:
    """Prompt for and parse a list of numbers from space- or comma-separated input.

    Returns:
        list[float] | None: List of numbers if valid, or None if input was invalid.
    """
    raw = input(f"{prompt_message}: ").strip()
    if not raw:
        return []

    # Replace commas with spaces to allow flexible user formats: "4, 7, 2" or "4 7 2"
    tokens = raw.replace(",", " ").split()
    numbers: list[float] = []

    for token in tokens:
        try:
            val = float(token)
            # If the float is an integer representation (e.g. 5.0), convert to int
            if val.is_integer():
                numbers.append(int(val))
            else:
                numbers.append(val)
        except ValueError:
            print(f"[Error] '{token}' is not a valid number. Please enter numeric values only.")
            return None

    return numbers


def parse_integer_list(prompt_message: str) -> list[int] | None:
    """Prompt for and parse a list of integers from space- or comma-separated input."""
    raw = input(f"{prompt_message}: ").strip()
    if not raw:
        return []

    tokens = raw.replace(",", " ").split()
    integers: list[int] = []

    for token in tokens:
        try:
            integers.append(int(token))
        except ValueError:
            print(f"[Error] '{token}' is not a valid integer. Please enter integers only.")
            return None

    return integers


def parse_key_value_pairs(prompt_message: str) -> dict[str, str] | None:
    """Parse key:value pairs separated by commas (e.g. 'a: 1, b: 2')."""
    print(prompt_message)
    raw = input("Enter pairs (e.g. key1:val1, key2:val2): ").strip()
    if not raw:
        return {}

    result: dict[str, str] = {}
    tokens = raw.split(",")
    for token in tokens:
        if ":" not in token:
            print(f"[Error] Invalid format in '{token.strip()}'. Expected 'key:value'.")
            return None
        key, val = token.split(":", 1)
        result[key.strip()] = val.strip()

    return result


# ---------------------------------------------------------------------------
# String Challenge Runners
# ---------------------------------------------------------------------------


def run_reverse_string() -> None:
    """Run Challenge 1: Reverse a String."""
    print_header("Challenge 1: Reverse a String")
    user_input = prompt_text("Enter a string to reverse")
    result = reverse_string(user_input)
    print(f"\n[Input]  : '{user_input}'")
    print(f"[Output] : '{result}'")


def run_count_vowels() -> None:
    """Run Challenge 2: Count Vowels."""
    print_header("Challenge 2: Count Vowels")
    user_input = prompt_text("Enter a sentence to count vowels (a, e, i, o, u)")
    count = count_vowels(user_input)
    print(f"\n[Input]  : '{user_input}'")
    print(f"[Output] : Total Vowels = {count}")


def run_check_palindrome() -> None:
    """Run Challenge 3: Check Palindrome."""
    print_header("Challenge 3: Check Palindrome")
    user_input = prompt_text("Enter a word or phrase to check")
    is_pal = is_palindrome(user_input)
    status = "Palindrome" if is_pal else "Not a Palindrome"
    print(f"\n[Input]  : '{user_input}'")
    print(f"[Output] : {status} (Result: {is_pal})")
    print("[Note]   : Ignores letter case and punctuation/spaces.")


def run_to_sentence_case() -> None:
    """Run Challenge 4: Sentence Case."""
    print_header("Challenge 4: Convert to Sentence Case")
    user_input = prompt_text("Enter a sentence")
    result = to_sentence_case(user_input)
    print(f"\n[Input]  : '{user_input}'")
    print(f"[Output] : '{result}'")


def run_word_frequency() -> None:
    """Run Challenge 5: Word Frequency."""
    print_header("Challenge 5: Word Frequency Counter")
    user_input = prompt_text("Enter a sentence to analyze word frequencies")
    freq = count_word_frequency(user_input)
    print(f"\n[Input]  : '{user_input}'")
    print("[Output] : Word Frequencies:")
    if not freq:
        print("  (No words detected)")
    else:
        for word, count in freq.items():
            print(f"  * '{word}': {count}")


def menu_strings() -> None:
    """Display the String Challenges submenu and route user selections."""
    while True:
        print_header("Category A: String Challenges")
        print("1. Reverse a String")
        print("2. Count Vowels")
        print("3. Check Palindrome")
        print("4. Convert Sentence to Sentence Case")
        print("5. Count Word Frequency")
        print("6. Back to Main Menu")

        choice = input("\nSelect a challenge (1-6): ").strip()
        if choice == "1":
            run_reverse_string()
        elif choice == "2":
            run_count_vowels()
        elif choice == "3":
            run_check_palindrome()
        elif choice == "4":
            run_to_sentence_case()
        elif choice == "5":
            run_word_frequency()
        elif choice == "6":
            break
        else:
            print("\n[Error] Invalid choice. Please enter a number between 1 and 6.")

        input("\nPress Enter to continue...")


# ---------------------------------------------------------------------------
# List Challenge Runners
# ---------------------------------------------------------------------------


def run_largest_and_smallest() -> None:
    """Run Challenge 1: Find Largest and Smallest."""
    print_header("Challenge 1: Largest and Smallest Numbers")
    numbers = parse_numeric_list("Enter numbers separated by spaces or commas (e.g. 4, 7, 2, 9, 5)")
    if numbers is None:
        return

    largest, smallest = find_largest_and_smallest(numbers)
    print(f"\n[Input List] : {numbers}")
    if largest is None:
        print("[Output]     : The list is empty. No largest or smallest values exist.")
    else:
        print(f"[Output]     : Largest = {largest}, Smallest = {smallest}")


def run_remove_duplicates() -> None:
    """Run Challenge 2: Remove Duplicates."""
    print_header("Challenge 2: Remove Duplicates")
    raw = input("Enter list items separated by spaces or commas (e.g. 4, 7, 2, 7, 9, 2): ").strip()
    if not raw:
        items = []
    else:
        items = raw.replace(",", " ").split()

    unique = remove_duplicates(items)
    print(f"\n[Original List] : {items}")
    print(f"[Unique List]   : {unique} (First occurrences preserved)")


def run_count_even_odd() -> None:
    """Run Challenge 3: Count Even and Odd."""
    print_header("Challenge 3: Count Even and Odd Numbers")
    integers = parse_integer_list("Enter integers separated by spaces or commas (e.g. 1, 2, 3, 4, 6)")
    if integers is None:
        return

    result = count_even_odd(integers)
    print(f"\n[Input List] : {integers}")
    print(f"[Output]     : Even = {result['even']}, Odd = {result['odd']}")


def run_bubble_sort() -> None:
    """Run Challenge 4: Bubble Sort."""
    print_header("Challenge 4: Bubble Sort (Without sort() or sorted())")
    numbers = parse_numeric_list("Enter numbers to sort (e.g. 64, 34, 25, 12, 22, 11, 90)")
    if numbers is None:
        return

    sorted_list = bubble_sort(numbers)
    print(f"\n[Unsorted List] : {numbers}")
    print(f"[Sorted List]   : {sorted_list}")


def run_find_common_elements() -> None:
    """Run Challenge 5: Find Common Elements."""
    print_header("Challenge 5: Common Elements Between Two Lists")
    raw1 = input("Enter List 1 items separated by commas/spaces: ").strip()
    raw2 = input("Enter List 2 items separated by commas/spaces: ").strip()

    list1 = raw1.replace(",", " ").split() if raw1 else []
    list2 = raw2.replace(",", " ").split() if raw2 else []

    common = find_common_elements(list1, list2)
    print(f"\n[List 1]          : {list1}")
    print(f"[List 2]          : {list2}")
    print(f"[Common Elements] : {common} (Duplicates removed, order preserved)")


def menu_lists() -> None:
    """Display the List Challenges submenu and route user selections."""
    while True:
        print_header("Category B: List Challenges")
        print("1. Find Largest and Smallest Numbers")
        print("2. Remove Duplicates")
        print("3. Count Even and Odd Numbers")
        print("4. Sort List (Bubble Sort)")
        print("5. Find Common Elements Between Two Lists")
        print("6. Back to Main Menu")

        choice = input("\nSelect a challenge (1-6): ").strip()
        if choice == "1":
            run_largest_and_smallest()
        elif choice == "2":
            run_remove_duplicates()
        elif choice == "3":
            run_count_even_odd()
        elif choice == "4":
            run_bubble_sort()
        elif choice == "5":
            run_find_common_elements()
        elif choice == "6":
            break
        else:
            print("\n[Error] Invalid choice. Please enter a number between 1 and 6.")

        input("\nPress Enter to continue...")


# ---------------------------------------------------------------------------
# Dictionary Challenge Runners
# ---------------------------------------------------------------------------


def run_character_frequency() -> None:
    """Run Challenge 1: Character Frequency."""
    print_header("Challenge 1: Character Frequency")
    text = prompt_text("Enter a string (e.g. 'banana')")
    freq = count_char_frequency(text, ignore_spaces=True)
    print(f"\n[Input String] : '{text}'")
    print(f"[Frequency]    : {freq}")
    print("[Note]         : Whitespace characters are ignored.")


def run_merge_dictionaries() -> None:
    """Run Challenge 2: Merge Two Dictionaries."""
    print_header("Challenge 2: Merge Two Dictionaries")
    print("Example: for Dict 1: a:1, b:2  |  for Dict 2: b:3, c:4")
    dict1 = parse_key_value_pairs("Enter Dictionary 1:")
    if dict1 is None:
        return
    dict2 = parse_key_value_pairs("Enter Dictionary 2 (keys will override Dict 1 on duplicate):")
    if dict2 is None:
        return

    merged = merge_dictionaries(dict1, dict2)
    print(f"\n[Dict 1] : {dict1}")
    print(f"[Dict 2] : {dict2}")
    print(f"[Merged] : {merged}")


def run_student_average() -> None:
    """Run Challenge 3: Student Marks Average."""
    print_header("Challenge 3: Student Marks Average")
    raw = input("Enter student:marks separated by commas (e.g. Ravi:80, Neha:90, Arjun:70): ").strip()
    if not raw:
        print("[Notice] Empty dictionary entered. Average = None (No records).")
        return

    marks: dict[str, float] = {}
    tokens = raw.split(",")
    for token in tokens:
        if ":" not in token:
            print(f"[Error] Invalid format in '{token}'. Expected 'StudentName:Marks'.")
            return
        name, score_str = token.split(":", 1)
        try:
            score = float(score_str.strip())
            marks[name.strip()] = score
        except ValueError:
            print(f"[Error] Score '{score_str.strip()}' for student '{name.strip()}' is not a valid number.")
            return

    try:
        avg = calculate_student_average(marks)
        print(f"\n[Student Marks] : {marks}")
        if avg is not None:
            print(f"[Output]        : Average Marks = {avg:.2f}")
    except ValueError as err:
        print(f"\n[Validation Error]: {err}")


def run_max_value_key() -> None:
    """Run Challenge 4: Key with Maximum Value."""
    print_header("Challenge 4: Find Key with Maximum Value")
    raw = input("Enter key:value pairs with numeric values (e.g. Math:95, English:88, Science:92): ").strip()
    if not raw:
        print("[Output] Key with Maximum Value: None (Empty dictionary)")
        return

    data: dict[str, float] = {}
    tokens = raw.split(",")
    for token in tokens:
        if ":" not in token:
            print(f"[Error] Invalid format in '{token}'. Expected 'key:numeric_value'.")
            return
        key, val_str = token.split(":", 1)
        try:
            data[key.strip()] = float(val_str.strip())
        except ValueError:
            print(f"[Error] Value '{val_str.strip()}' is not numeric.")
            return

    best_key = find_key_with_max_value(data)
    print(f"\n[Dictionary] : {data}")
    print(f"[Output]     : Key with Maximum Value = '{best_key}' (Value: {data[best_key]})")


def run_group_by_category() -> None:
    """Run Challenge 5: Group Values by Category."""
    print_header("Challenge 5: Group Values by Category")
    print("Example input: apple:fruit, carrot:vegetable, banana:fruit, spinach:vegetable")
    raw = input("Enter item:category pairs separated by commas: ").strip()
    if not raw:
        print("[Output] Grouped items: {}")
        return

    pairs: list[tuple[str, str]] = []
    tokens = raw.split(",")
    for token in tokens:
        if ":" not in token:
            print(f"[Error] Invalid format in '{token}'. Expected 'item:category'.")
            return
        item, category = token.split(":", 1)
        pairs.append((item.strip(), category.strip()))

    grouped = group_by_category(pairs)
    print("\n[Grouped Results]:")
    for category, items in grouped.items():
        print(f"  * {category}: {items}")


def menu_dictionaries() -> None:
    """Display the Dictionary Challenges submenu and route user selections."""
    while True:
        print_header("Category C: Dictionary Challenges")
        print("1. Character Frequency Count")
        print("2. Merge Two Dictionaries")
        print("3. Student Marks Average")
        print("4. Find Key with Maximum Value")
        print("5. Group Values by Category")
        print("6. Back to Main Menu")

        choice = input("\nSelect a challenge (1-6): ").strip()
        if choice == "1":
            run_character_frequency()
        elif choice == "2":
            run_merge_dictionaries()
        elif choice == "3":
            run_student_average()
        elif choice == "4":
            run_max_value_key()
        elif choice == "5":
            run_group_by_category()
        elif choice == "6":
            break
        else:
            print("\n[Error] Invalid choice. Please enter a number between 1 and 6.")

        input("\nPress Enter to continue...")


# ---------------------------------------------------------------------------
# Main Menu Controller
# ---------------------------------------------------------------------------


def main() -> None:
    """Main program entry point with top-level navigation loop."""
    try:
        while True:
            print_header("PYTHON MINI CHALLENGES - WEEK 1 TASK 3")
            print("1. String Challenges")
            print("2. List Challenges")
            print("3. Dictionary Challenges")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ").strip()
            if choice == "1":
                menu_strings()
            elif choice == "2":
                menu_lists()
            elif choice == "3":
                menu_dictionaries()
            elif choice == "4":
                print("\nThank you for exploring Python Mini Challenges! Exiting safely...")
                sys.exit(0)
            else:
                print(f"\n[Error] Invalid choice '{choice}'. Please select a valid option (1-4).")
                input("Press Enter to continue...")
    except (KeyboardInterrupt, EOFError):
        print("\n\nOperation cancelled by user. Exiting safely. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
