def vowels_count(s):
    """
    Counts the number of vowels in a given string, considering 'y' as a vowel at the end of the word.

    Args:
    s (str): The input string to count vowels in.

    Returns:
    int: The number of vowels in the input string.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Define a list of vowels (both lowercase and uppercase) and a special case for 'y'
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'Y']

    # Initialize a counter variable to store the number of vowels found
    count = 0

    # Iterate through each character in the input string
    for i in range(len(s)):
        # Check if the character is a vowel (case-insensitive)
        if s[i] in vowels:
            # Increment the counter
            count += 1

        # Check if the character is 'y' and it's the last character in the string
        if s[i] == 'y' and i == len(s) - 1:
            # Increment the counter
            count += 1

    # Return the final count of vowels
    return count