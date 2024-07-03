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
    

    Action Plan:
    1. Normalize input strings:
        - Convert all characters to a uniform case (lowercase or uppercase)
    
    2. Create a data structure to count character occurrences:
        - Initialize a dictionary to store character counts
    
    3. Iterate over the first input string:
        - Update the character count dictionary
    
    4. Iterate over the second input string:
        - Update the character count dictionary
    
    5. Compare the character count dictionaries of both strings:
        - Check if they are equal
    
    6. Edge cases:
        - Handle strings of different lengths
        - Ignore characters not present in one of the strings
    
    7. Summary of the steps:
        - Normalize strings
        - Count characters in both
        - Compare character count dictionaries
        - Return boolean result
    """
    # Normalize input strings
    s0 = s0.lower()
    s1 = s1.lower()
    
    # Create a data structure to count character occurrences
    char_count_s0 = {}
    char_count_s1 = {}
    
    # Iterate over the first input string
    for char in s0:
        if char in char_count_s0:
            char_count_s0[char] += 1
        else:
            char_count_s0[char] = 1
    
    # Iterate over the second input string
    for char in s1:
        if char in char_count_s1:
            char_count_s1[char] += 1
        else:
            char_count_s1[char] = 1
    
    # Compare the character count dictionaries of both strings
    return char_count_s0 == char_count_s1