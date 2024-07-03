def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    
    Args:
    s0 (str): The first input string.
    s1 (str): The second input string.
    
    Returns:
    bool: True if the two input strings have the same characters, False otherwise.
    
    Examples:
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Step 1: Preprocess the input strings
    s0 = s0.lower()
    s1 = s1.lower()
    
    # Step 2: Compare the characters in both strings
    set_s0 = set(s0)
    set_s1 = set(s1)
    
    # Step 3: Return the result
    return set_s0 == set_s1