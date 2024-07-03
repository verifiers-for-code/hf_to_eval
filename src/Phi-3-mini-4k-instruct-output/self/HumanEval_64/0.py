def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Define a list of vowels, including 'y' as a vowel at the end
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in vowels:
            # Increment the counter
            vowel_count += 1
        # Special handling for 'y' at the end
        elif char == 'y' and i == len(s) - 1:
            # Increment the counter
            vowel_count += 1

    # Return the vowel count
    return vowel_count