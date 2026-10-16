"""Unit tests for List Operation challenges."""

import sys
import unittest
from pathlib import Path

# Ensure root package directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lists import (
    bubble_sort,
    count_even_odd,
    find_common_elements,
    find_largest_and_smallest,
    remove_duplicates,
)


class TestListChallenges(unittest.TestCase):
    """Test suite for functions in lists.py."""

    # -------------------------------------------------------------------------
    # Challenge 1: find_largest_and_smallest
    # -------------------------------------------------------------------------
    def test_find_largest_and_smallest_normal(self):
        """Test finding largest and smallest in standard list."""
        self.assertEqual(find_largest_and_smallest([4, 7, 2, 9, 5]), (9, 2))

    def test_find_largest_and_smallest_negative_and_zero(self):
        """Test finding min/max with negative numbers and zero."""
        self.assertEqual(find_largest_and_smallest([-10, 0, 25, -35, 12]), (25, -35))

    def test_find_largest_and_smallest_floats(self):
        """Test finding min/max with floating point numbers."""
        self.assertEqual(find_largest_and_smallest([1.5, 4.2, 0.3, 9.8]), (9.8, 0.3))

    def test_find_largest_and_smallest_single_element(self):
        """Test single-element list returns that element as both min and max."""
        self.assertEqual(find_largest_and_smallest([42]), (42, 42))

    def test_find_largest_and_smallest_empty(self):
        """Test empty list returns (None, None)."""
        self.assertEqual(find_largest_and_smallest([]), (None, None))

    # -------------------------------------------------------------------------
    # Challenge 2: remove_duplicates
    # -------------------------------------------------------------------------
    def test_remove_duplicates_normal(self):
        """Test removing duplicates while preserving original order."""
        self.assertEqual(remove_duplicates([4, 7, 2, 7, 9, 2]), [4, 7, 2, 9])

    def test_remove_duplicates_no_duplicates(self):
        """Test list with all unique elements is unchanged."""
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_all_identical(self):
        """Test list where all elements are identical."""
        self.assertEqual(remove_duplicates([5, 5, 5, 5]), [5])

    def test_remove_duplicates_strings(self):
        """Test removing duplicates from string list."""
        self.assertEqual(
            remove_duplicates(["apple", "banana", "apple", "orange", "banana"]),
            ["apple", "banana", "orange"],
        )

    def test_remove_duplicates_empty(self):
        """Test empty list returns empty list."""
        self.assertEqual(remove_duplicates([]), [])

    # -------------------------------------------------------------------------
    # Challenge 3: count_even_odd
    # -------------------------------------------------------------------------
    def test_count_even_odd_normal(self):
        """Test counting even and odd integers in mixed list."""
        self.assertEqual(count_even_odd([1, 2, 3, 4, 6]), {"even": 3, "odd": 2})

    def test_count_even_odd_all_even(self):
        """Test list containing only even integers."""
        self.assertEqual(count_even_odd([2, 4, 6, 8, 10]), {"even": 5, "odd": 0})

    def test_count_even_odd_all_odd(self):
        """Test list containing only odd integers."""
        self.assertEqual(count_even_odd([1, 3, 5, 7, 9]), {"even": 0, "odd": 5})

    def test_count_even_odd_negatives_and_zero(self):
        """Test counting handles zero (even) and negative numbers."""
        self.assertEqual(count_even_odd([-4, -3, 0, 5]), {"even": 2, "odd": 2})

    def test_count_even_odd_empty(self):
        """Test empty list returns zeros."""
        self.assertEqual(count_even_odd([]), {"even": 0, "odd": 0})

    # -------------------------------------------------------------------------
    # Challenge 4: bubble_sort
    # -------------------------------------------------------------------------
    def test_bubble_sort_normal(self):
        """Test sorting an unsorted list of numbers."""
        data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(data), expected)

    def test_bubble_sort_already_sorted(self):
        """Test list that is already sorted."""
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_bubble_sort_reverse_sorted(self):
        """Test list in reverse descending order."""
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_bubble_sort_with_negatives_and_duplicates(self):
        """Test sorting with negative values and duplicate numbers."""
        self.assertEqual(bubble_sort([3, -1, 4, -1, 5, 0]), [-1, -1, 0, 3, 4, 5])

    def test_bubble_sort_preserves_original(self):
        """Test bubble_sort does not mutate original input list."""
        original = [3, 2, 1]
        _ = bubble_sort(original)
        self.assertEqual(original, [3, 2, 1])

    def test_bubble_sort_empty_and_single(self):
        """Test sorting empty and single-element lists."""
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([42]), [42])

    # -------------------------------------------------------------------------
    # Challenge 5: find_common_elements
    # -------------------------------------------------------------------------
    def test_find_common_elements_normal(self):
        """Test finding common elements without duplicating common results."""
        list1 = [1, 2, 2, 3, 4]
        list2 = [2, 3, 5]
        self.assertEqual(find_common_elements(list1, list2), [2, 3])

    def test_find_common_elements_no_overlap(self):
        """Test two lists with no common items."""
        self.assertEqual(find_common_elements([1, 2], [3, 4]), [])

    def test_find_common_elements_empty_inputs(self):
        """Test handling empty lists."""
        self.assertEqual(find_common_elements([], [1, 2]), [])
        self.assertEqual(find_common_elements([1, 2], []), [])
        self.assertEqual(find_common_elements([], []), [])


if __name__ == "__main__":
    unittest.main()
