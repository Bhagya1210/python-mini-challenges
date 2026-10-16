"""Unit tests for Dictionary challenges."""

import sys
import unittest
from pathlib import Path

# Ensure root package directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dictionaries import (
    calculate_student_average,
    count_char_frequency,
    find_key_with_max_value,
    group_by_category,
    merge_dictionaries,
)


class TestDictionaryChallenges(unittest.TestCase):
    """Test suite for functions in dictionaries.py."""

    # -------------------------------------------------------------------------
    # Challenge 1: count_char_frequency
    # -------------------------------------------------------------------------
    def test_count_char_frequency_normal(self):
        """Test counting character frequency in normal word."""
        result = count_char_frequency("banana")
        self.assertEqual(result, {"b": 1, "a": 3, "n": 2})

    def test_count_char_frequency_ignore_spaces(self):
        """Test ignoring spaces by default."""
        result = count_char_frequency("a b a")
        self.assertEqual(result, {"a": 2, "b": 1})

    def test_count_char_frequency_keep_spaces(self):
        """Test preserving spaces when ignore_spaces=False."""
        result = count_char_frequency("a b", ignore_spaces=False)
        self.assertEqual(result, {"a": 1, " ": 1, "b": 1})

    def test_count_char_frequency_empty(self):
        """Test empty string returns empty dictionary."""
        self.assertEqual(count_char_frequency(""), {})

    # -------------------------------------------------------------------------
    # Challenge 2: merge_dictionaries
    # -------------------------------------------------------------------------
    def test_merge_dictionaries_with_overlap(self):
        """Test merging two dictionaries where dict2 overwrites dict1 keys."""
        d1 = {"a": 1, "b": 2}
        d2 = {"b": 3, "c": 4}
        merged = merge_dictionaries(d1, d2)
        self.assertEqual(merged, {"a": 1, "b": 3, "c": 4})

    def test_merge_dictionaries_preserves_originals(self):
        """Test original dictionaries remain unmutated."""
        d1 = {"x": 10}
        d2 = {"y": 20}
        _ = merge_dictionaries(d1, d2)
        self.assertEqual(d1, {"x": 10})
        self.assertEqual(d2, {"y": 20})

    def test_merge_dictionaries_with_empty(self):
        """Test merging with empty dictionaries."""
        self.assertEqual(merge_dictionaries({"a": 1}, {}), {"a": 1})
        self.assertEqual(merge_dictionaries({}, {"b": 2}), {"b": 2})
        self.assertEqual(merge_dictionaries({}, {}), {})

    # -------------------------------------------------------------------------
    # Challenge 3: calculate_student_average
    # -------------------------------------------------------------------------
    def test_calculate_student_average_normal(self):
        """Test standard student marks average calculation."""
        marks = {"Ravi": 80, "Neha": 90, "Arjun": 70}
        self.assertEqual(calculate_student_average(marks), 80.0)

    def test_calculate_student_average_decimals(self):
        """Test average rounded to two decimal places."""
        marks = {"Alice": 85, "Bob": 90, "Charlie": 91}
        # (85 + 90 + 91) / 3 = 266 / 3 = 88.6666... -> 88.67
        self.assertEqual(calculate_student_average(marks), 88.67)

    def test_calculate_student_average_empty(self):
        """Test empty dictionary returns None."""
        self.assertIsNone(calculate_student_average({}))

    def test_calculate_student_average_invalid_string_marks(self):
        """Test non-numeric marks raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_student_average({"Alice": "eighty", "Bob": 90})

    def test_calculate_student_average_negative_marks(self):
        """Test negative marks raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_student_average({"Alice": -15, "Bob": 90})

    # -------------------------------------------------------------------------
    # Challenge 4: find_key_with_max_value
    # -------------------------------------------------------------------------
    def test_find_key_with_max_value_normal(self):
        """Test finding key with maximum numeric score."""
        scores = {"Math": 95, "English": 88, "Science": 92}
        self.assertEqual(find_key_with_max_value(scores), "Math")

    def test_find_key_with_max_value_negative_numbers(self):
        """Test finding maximum among negative values."""
        data = {"temp1": -15, "temp2": -5, "temp3": -20}
        self.assertEqual(find_key_with_max_value(data), "temp2")

    def test_find_key_with_max_value_empty(self):
        """Test empty dictionary returns None."""
        self.assertIsNone(find_key_with_max_value({}))

    # -------------------------------------------------------------------------
    # Challenge 5: group_by_category
    # -------------------------------------------------------------------------
    def test_group_by_category_from_tuples(self):
        """Test grouping items from list of tuples."""
        pairs = [
            ("apple", "fruit"),
            ("carrot", "vegetable"),
            ("banana", "fruit"),
            ("broccoli", "vegetable"),
        ]
        expected = {
            "fruit": ["apple", "banana"],
            "vegetable": ["carrot", "broccoli"],
        }
        self.assertEqual(group_by_category(pairs), expected)

    def test_group_by_category_from_dict(self):
        """Test grouping items when provided as a dictionary."""
        mapping = {"apple": "fruit", "carrot": "vegetable", "banana": "fruit"}
        expected = {
            "fruit": ["apple", "banana"],
            "vegetable": ["carrot"],
        }
        self.assertEqual(group_by_category(mapping), expected)

    def test_group_by_category_empty(self):
        """Test grouping empty input returns empty dict."""
        self.assertEqual(group_by_category([]), {})
        self.assertEqual(group_by_category({}), {})


if __name__ == "__main__":
    unittest.main()
