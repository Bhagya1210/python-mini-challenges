"""String Manipulation Challenges.

This module provides beginner-friendly, reusable functions for common
string processing challenges:
1. Reversing a string
2. Counting vowels (case-insensitive)
3. Checking for palindromes
4. Converting a sentence to sentence case
5. Counting word frequencies with punctuation normalization
"""

import string


def reverse_string(text: str) -> str:
    """Reverse a given string using Python slicing.

    Approach:
        Python's slice notation `[start:stop:step]` with a step of `-1`
        efficiently traverses the sequence backward from the last character
        to the first.

    Args:
        text (str): The input string to reverse.

    Returns:
        str: The reversed string. Returns an empty string if input is empty.

    Example:
        >>> reverse_string("python")
        'nohtyp'
        >>> reverse_string("")
        ''
    """
    if not text:
        return ""
    return text[::-1]


def count_vowels(sentence: str) -> int:
    """Count the total number of vowels in a string (case-insensitive).

    Approach:
        Converts the text to lowercase and iterates through each character,
        checking if it is in the vowel set ('a', 'e', 'i', 'o', 'u').

    Args:
        sentence (str): The input string or sentence.

    Returns:
        int: The total count of vowels. Returns 0 for empty or vowel-less strings.

    Example:
        >>> count_vowels("Python Internship")
        4
        >>> count_vowels("rhythm")
        0
    """
    if not sentence:
        return 0

    vowels = {"a", "e", "i", "o", "u"}
    vowel_count = 0
    for char in sentence.lower():
        if char in vowels:
            vowel_count += 1

    return vowel_count


def is_palindrome(text: str) -> bool:
    """Check whether a string is a palindrome.

    Approach:
        1. Strips leading and trailing whitespace.
        2. Normalizes case to lowercase.
        3. Removes internal spaces and punctuation to verify genuine palindromes
           (e.g., "Madam", "race car", or "A man, a plan, a canal: Panama").
        4. Compares the cleaned string with its reverse.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
              Returns False for empty strings or strings with no alphanumeric characters.

    Example:
        >>> is_palindrome("Madam")
        True
        >>> is_palindrome("race car")
        True
        >>> is_palindrome("python")
        False
    """
    if not text:
        return False

    # Extract only alphanumeric characters in lowercase
    cleaned = "".join(char.lower() for char in text if char.isalnum())

    if not cleaned:
        return False

    return cleaned == cleaned[::-1]


def to_sentence_case(sentence: str) -> str:
    """Convert a sentence to standard sentence case.

    Approach:
        Strips surrounding whitespace, capitalizes the first character,
        and converts all subsequent characters to lowercase.

    Args:
        sentence (str): The input string to convert.

    Returns:
        str: The sentence formatted with an initial uppercase letter
             and the rest in lowercase. Returns empty string if input is empty.

    Example:
        >>> to_sentence_case("hELLO wORLD")
        'Hello world'
        >>> to_sentence_case("   python IS awesome!   ")
        'Python is awesome!'
    """
    stripped = sentence.strip()
    if not stripped:
        return ""

    return stripped[0].upper() + stripped[1:].lower()


def count_word_frequency(sentence: str) -> dict[str, int]:
    """Count the frequency of each word in a sentence.

    Approach:
        1. Strips punctuation characters from the text.
        2. Converts text to lowercase for consistent, case-insensitive counting.
        3. Splits the text into individual words on whitespace.
        4. Tallies word occurrences using a dictionary.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict[str, int]: A dictionary mapping each unique word to its frequency.
                        Returns an empty dictionary for empty or whitespace-only input.

    Example:
        >>> count_word_frequency("Python is great, python is fun!")
        {'python': 2, 'is': 2, 'great': 1, 'fun': 1}
    """
    if not sentence or not sentence.strip():
        return {}

    # Replace punctuation characters with spaces so words adjacent to punctuation are clean
    clean_text = ""
    for char in sentence:
        if char in string.punctuation:
            clean_text += " "
        else:
            clean_text += char

    words = clean_text.lower().split()
    frequency: dict[str, int] = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency
