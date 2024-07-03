def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Args:
    test (str): A string of space separated lowercase letters.

    Returns:
    dict: A dictionary containing the letter(s) with the most repetition and their count.

    Example:
    >>> histogram('a b c')
    {'a': 1, 'b': 1, 'c': 1}
    >>> histogram('a b b a')
    {'a': 2, 'b': 2}
    >>> histogram('a b c a b')
    {'a': 2, 'b': 2}
    >>> histogram('b b b b a')
    {'b': 4}
    >>> histogram('')
    {}
    """
    # Step 1: Initialize an empty dictionary to store the letter counts.
    letter_counts = {}

    # Step 2: Iterate through each character in the input string.
    for char in test.split():
        # Step 2a: If the character is a lowercase letter, increment its count in the dictionary.
        if char.islower():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Step 3: Find the maximum count among all letter counts.
    max_count = max(letter_counts.values())

    # Step 4: Create a new dictionary to store the result.
    result = {letter: count for letter, count in letter_counts.items() if count == max_count}

    # Return the result dictionary.
    return result