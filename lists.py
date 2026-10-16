"""List Operation Challenges.

This module provides beginner-friendly, reusable functions for common
list processing challenges:
1. Finding the largest and smallest numbers
2. Removing duplicate elements while preserving original order
3. Counting even and odd numbers
4. Sorting a list using Bubble Sort (without built-in sort/sorted)
5. Finding common elements between two lists without duplicates
"""

from typing import Any


def find_largest_and_smallest(
    numbers: list[int | float],
) -> tuple[int | float | None, int | float | None]:
    """Find the largest and smallest values in a list of numbers.

    Approach:
        Initializes `largest` and `smallest` with the first element of the list.
        Iterates sequentially through the remaining numbers, updating `largest`
        if a greater value is found and `smallest` if a lower value is found.
        This provides an O(n) single-pass scan.

    Args:
        numbers (list[int | float]): A list containing numeric elements.

    Returns:
        tuple[int | float | None, int | float | None]:
            A tuple of (largest, smallest). Returns (None, None) if the list is empty.

    Example:
        >>> find_largest_and_smallest([4, 7, 2, 9, 5])
        (9, 2)
        >>> find_largest_and_smallest([])
        (None, None)
    """
    if not numbers:
        return (None, None)

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return (largest, smallest)


def remove_duplicates(items: list[Any]) -> list[Any]:
    """Remove duplicate elements from a list while preserving original order.

    Approach:
        Uses a helper `seen` set for O(1) membership lookups alongside an
        `output` list. As we iterate through `items`, an element is added to
        `output` only if it has not yet been recorded in `seen`.

    Args:
        items (list[Any]): The input list containing elements.

    Returns:
        list[Any]: A new list containing unique elements in their first-seen order.

    Example:
        >>> remove_duplicates([4, 7, 2, 7, 9, 2])
        [4, 7, 2, 9]
        >>> remove_duplicates([])
        []
    """
    if not items:
        return []

    seen = set()
    unique_items: list[Any] = []

    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)

    return unique_items


def count_even_odd(numbers: list[int]) -> dict[str, int]:
    """Count the total number of even and odd integers in a list.

    Approach:
        Iterates over the integer list and uses the modulo operator `% 2`:
        - `num % 2 == 0` signifies an even integer.
        - Otherwise, the integer is odd.
        Tallies the respective totals in a dictionary.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        dict[str, int]: A dictionary with keys 'even' and 'odd' representing counts.
                        Returns {'even': 0, 'odd': 0} if the list is empty.

    Example:
        >>> count_even_odd([1, 2, 3, 4, 6])
        {'even': 3, 'odd': 2}
        >>> count_even_odd([])
        {'even': 0, 'odd': 0}
    """
    counts = {"even": 0, "odd": 0}

    for num in numbers:
        if num % 2 == 0:
            counts["even"] += 1
        else:
            counts["odd"] += 1

    return counts


def bubble_sort(numbers: list[int | float]) -> list[int | float]:
    """Sort a list in ascending order using the Bubble Sort algorithm.

    Approach:
        Bubble sort repeatedly steps through the list, compares adjacent elements,
        and swaps them if they are in the wrong order (left > right).
        This pass is repeated until no swaps are needed.
        Creates a copy of the input list to avoid modifying the caller's list.

    Args:
        numbers (list[int | float]): A list of numeric values.

    Returns:
        list[int | float]: A new list sorted in ascending order.

    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> bubble_sort([])
        []
    """
    # Create a shallow copy to preserve original list immutability
    sorted_list = list(numbers)
    n = len(sorted_list)

    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap elements
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True
        # If no swaps occurred during the pass, the list is already sorted
        if not swapped:
            break

    return sorted_list


def find_common_elements(list1: list[Any], list2: list[Any]) -> list[Any]:
    """Find common elements between two lists without duplicating results.

    Approach:
        Converts the second list into a set for O(1) membership checks.
        Iterates over `list1` and records an element in the result list if it
        exists in `set2` and has not already been added to the result.
        This preserves the order of first appearance from `list1`.

    Args:
        list1 (list[Any]): The first list.
        list2 (list[Any]): The second list.

    Returns:
        list[Any]: A list containing distinct common elements in original order.

    Example:
        >>> find_common_elements([1, 2, 2, 3, 4], [2, 3, 5])
        [2, 3]
        >>> find_common_elements([], [1, 2])
        []
    """
    if not list1 or not list2:
        return []

    set2 = set(list2)
    common: list[Any] = []
    seen = set()

    for item in list1:
        if item in set2 and item not in seen:
            seen.add(item)
            common.append(item)

    return common
