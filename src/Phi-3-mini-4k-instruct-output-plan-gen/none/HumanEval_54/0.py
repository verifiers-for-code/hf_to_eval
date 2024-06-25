
from collections import Counter

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    # Count the characters in both strings
    count_s0 = Counter(s0)
    count_s1 = Counter(s1)

    # Check if the character counts are equal
    return count_s0 == count_s1