def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Step 1: Normalize input strings
    s0 = s0.lower()
    s1 = s1.lower()

    # Step 2: Create a data structure to count character occurrences
    char_count_s0 = {}
    char_count_s1 = {}

    # Step 3 & 4: Iterate over the first and second input strings
    for char in s0:
        if char in char_count_s0:
            char_count_s0[char] += 1
        else:
            char_count_s0[char] = 1

    for char in s1:
        if char in char_count_s1:
            char_count_s1[char] += 1
        else:
            char_count_s1[char] = 1

    # Step 5: Compare the character count dictionaries of both strings
    return char_count_s0 == char_count_s1