def vowels_count(s):
    """
    Counts the number of vowels in a given string, considering 'y' as a vowel only when it's at the end of the word.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Define a list of vowels, including 'y' as a vowel at the end
    vowels = ['a', 'e', 'i', 'o', 'u']
    special_vowel = 'y'

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through the string
    for i in range(len(s)):
        # Check if the current character is a vowel
        if s[i].lower() in vowels:
            vowel_count += 1

        # Special handling for 'y' at the end
        if i == len(s) - 1 and s[i].lower() == special_vowel:
            vowel_count += 1

    return vowel_count