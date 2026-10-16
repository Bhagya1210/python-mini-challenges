"""Dictionary Challenges.

This module provides beginner-friendly, reusable functions for key-value
data processing:
1. Counting character frequency
2. Merging two dictionaries (handling duplicate keys safely)
3. Calculating student marks average with input validation
4. Finding the key associated with the maximum value
5. Grouping values by category into a dictionary
"""

from typing import Any


def count_char_frequency(text: str, ignore_spaces: bool = True) -> dict[str, int]:
    """Count how many times each character occurs in a string.

    Approach:
        Iterates character by character. If `ignore_spaces` is True, whitespace
        characters are skipped. Counts are accumulated in a dictionary.

    Args:
        text (str): The input string to inspect.
        ignore_spaces (bool, optional): Whether to ignore whitespace. Defaults to True.

    Returns:
        dict[str, int]: A dictionary mapping characters to their frequencies.
                        Returns an empty dictionary for empty input.

    Example:
        >>> count_char_frequency("banana")
        {'b': 1, 'a': 3, 'n': 2}
        >>> count_char_frequency("a b c", ignore_spaces=False)
        {'a': 1, ' ': 2, 'b': 1, 'c': 1}
    """
    if not text:
        return {}

    frequency: dict[str, int] = {}
    for char in text:
        if ignore_spaces and char.isspace():
            continue
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


def merge_dictionaries(dict1: dict[Any, Any], dict2: dict[Any, Any]) -> dict[Any, Any]:
    """Merge two dictionaries into a new dictionary without mutating originals.

    Duplicate Key Policy:
        Values from `dict2` will overwrite values from `dict1` if duplicate
        keys exist, following standard Python dictionary merging behavior.

    Args:
        dict1 (dict[Any, Any]): The primary dictionary.
        dict2 (dict[Any, Any]): The secondary dictionary whose keys take precedence.

    Returns:
        dict[Any, Any]: A new merged dictionary containing key-value pairs from both.

    Example:
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    merged = dict(dict1)
    merged.update(dict2)
    return merged


def calculate_student_average(marks: dict[str, int | float]) -> float | None:
    """Calculate the average marks from a dictionary of student names and marks.

    Approach:
        Validates that all marks are valid numbers (int or float) and non-negative.
        Calculates the arithmetic mean: sum(marks) / count(students)
        and rounds the result to 2 decimal places.

    Args:
        marks (dict[str, int | float]): Mapping of student names to numeric marks.

    Returns:
        float | None: The average marks rounded to 2 decimal places, or None if the
                      dictionary is empty.

    Raises:
        ValueError: If any student mark is not numeric or is negative.

    Example:
        >>> calculate_student_average({'Ravi': 80, 'Neha': 90, 'Arjun': 70})
        80.0
        >>> calculate_student_average({})
        None
    """
    if not marks:
        return None

    total = 0.0
    for student, mark in marks.items():
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise ValueError(f"Invalid mark for student '{student}': {mark}. Marks must be numeric.")
        if mark < 0:
            raise ValueError(f"Invalid negative mark for student '{student}': {mark}.")
        total += mark

    average = total / len(marks)
    return round(average, 2)


def find_key_with_max_value(data: dict[Any, int | float]) -> Any | None:
    """Find the key associated with the maximum value in a dictionary.

    Approach:
        Iterates over key-value pairs, tracking the maximum value seen so far
        and its corresponding key. If multiple keys share the maximum value,
        the first one encountered is returned.

    Args:
        data (dict[Any, int | float]): A dictionary containing comparable values.

    Returns:
        Any | None: The key with the highest value, or None if dictionary is empty.

    Raises:
        TypeError: If dictionary values cannot be compared with each other.

    Example:
        >>> find_key_with_max_value({'Math': 95, 'English': 88, 'Science': 92})
        'Math'
        >>> find_key_with_max_value({})
        None
    """
    if not data:
        return None

    max_key = None
    max_val = None

    for key, val in data.items():
        if max_val is None or val > max_val:
            max_val = val
            max_key = key

    return max_key


def group_by_category(items: list[tuple[str, str]] | dict[str, str]) -> dict[str, list[str]]:
    """Group items by category into a dictionary.

    Approach:
        Accepts either a list of `(item_name, category)` tuples or a dictionary
        mapping `{item_name: category}`.
        Groups each item into a list corresponding to its category key.

    Args:
        items (list[tuple[str, str]] | dict[str, str]): Items paired with their categories.

    Returns:
        dict[str, list[str]]: A dictionary where each key is a category and value is
                              a list of item names belonging to that category.

    Example:
        >>> pairs = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit')]
        >>> group_by_category(pairs)
        {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}
    """
    if not items:
        return {}

    grouped: dict[str, list[str]] = {}

    # Handle dictionary input: {item: category}
    if isinstance(items, dict):
        iterable = items.items()
    else:
        iterable = items

    for item, category in iterable:
        category_str = str(category).strip()
        item_str = str(item).strip()
        if category_str not in grouped:
            grouped[category_str] = []
        grouped[category_str].append(item_str)

    return grouped
