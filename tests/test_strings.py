"""Unit tests for String Manipulation challenges."""

import sys
import unittest
from pathlib import Path

# Ensure root package directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strings import (
    count_vowels,
    count_word_frequency,
    is_palindrome,
    reverse_string,
    to_sentence_case,
)


class TestStringChallenges(unittest.TestCase):
    """Test suite for functions in strings.py."""

    # -------------------------------------------------------------------------
    # Challenge 1: reverse_string
    # -------------------------------------------------------------------------
    def test_reverse_string_normal(self):
        """Test reversing standard words."""
        self.assertEqual(reverse_string("python"), "nohtyp")
        self.assertEqual(reverse_string("Internship"), "pihsnretnI")

    def test_reverse_string_empty(self):
        """Test reversing empty string returns empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_single_char(self):
        """Test reversing single-character string."""
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_with_spaces_and_symbols(self):
        """Test reversing strings with spaces and punctuation."""
        self.assertEqual(reverse_string("hello world!"), "!dlrow olleh")

    # -------------------------------------------------------------------------
    # Challenge 2: count_vowels
    # -------------------------------------------------------------------------
    def test_count_vowels_normal(self):
        """Test vowel counting on standard sentences."""
        self.assertEqual(count_vowels("Python Internship"), 4)

    def test_count_vowels_case_insensitivity(self):
        """Test vowel counting handles uppercase and lowercase identically."""
        self.assertEqual(count_vowels("AEIOU aeiou"), 10)

    def test_count_vowels_no_vowels(self):
        """Test vowel count when no vowels are present."""
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("bcdfg123!"), 0)

    def test_count_vowels_empty(self):
        """Test vowel count on empty input returns 0."""
        self.assertEqual(count_vowels(""), 0)

    # -------------------------------------------------------------------------
    # Challenge 3: is_palindrome
    # -------------------------------------------------------------------------
    def test_is_palindrome_simple(self):
        """Test simple single-word palindromes."""
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_case_insensitive(self):
        """Test palindromes with mixed casing."""
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("Deed"))

    def test_is_palindrome_with_spaces_and_punctuation(self):
        """Test palindromic phrases containing spaces and punctuation."""
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_is_palindrome_false_cases(self):
        """Test non-palindromes return False."""
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("internship"))

    def test_is_palindrome_empty_and_whitespace(self):
        """Test empty string and whitespace-only strings return False."""
        self.assertFalse(is_palindrome(""))
        self.assertFalse(is_palindrome("   "))
        self.assertFalse(is_palindrome(" ,:!? "))

    # -------------------------------------------------------------------------
    # Challenge 4: to_sentence_case
    # -------------------------------------------------------------------------
    def test_to_sentence_case_all_uppercase(self):
        """Test converting all-uppercase sentence."""
        self.assertEqual(to_sentence_case("HELLO WORLD"), "Hello world")

    def test_to_sentence_case_all_lowercase(self):
        """Test converting all-lowercase sentence."""
        self.assertEqual(to_sentence_case("python programming"), "Python programming")

    def test_to_sentence_case_leading_trailing_spaces(self):
        """Test sentence case ignores leading/trailing whitespace."""
        self.assertEqual(to_sentence_case("   weIntern Python   "), "Weintern python")

    def test_to_sentence_case_empty(self):
        """Test sentence case on empty string returns empty string."""
        self.assertEqual(to_sentence_case(""), "")
        self.assertEqual(to_sentence_case("   "), "")

    # -------------------------------------------------------------------------
    # Challenge 5: count_word_frequency
    # -------------------------------------------------------------------------
    def test_count_word_frequency_normal(self):
        """Test counting word frequencies with repeated words."""
        sentence = "Python is great, python is fun!"
        expected = {"python": 2, "is": 2, "great": 1, "fun": 1}
        self.assertEqual(count_word_frequency(sentence), expected)

    def test_count_word_frequency_punctuation_stripping(self):
        """Test word frequency correctly separates words connected by punctuation."""
        sentence = "apple, banana; apple! orange? banana."
        expected = {"apple": 2, "banana": 2, "orange": 1}
        self.assertEqual(count_word_frequency(sentence), expected)

    def test_count_word_frequency_empty(self):
        """Test word frequency on empty or whitespace strings returns empty dict."""
        self.assertEqual(count_word_frequency(""), {})
        self.assertEqual(count_word_frequency("   \t\n  "), {})


if __name__ == "__main__":
    unittest.main()
