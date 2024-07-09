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
    1. Define a function `same_chars` that takes two strings `s0` and `s1` as input.
    2. Initialize two empty dictionaries `char_count0` and `char_count1` to store character counts for `s0` and `s1`, respectively.
    3. Iterate through each character in `s0`:
        a. If the character is already in `char_count0`, increment its count.
        b. If the character is not in `char_count0`, add it with a count of 1.
    4. Iterate through each character in `s1`:
        a. If the character is already in `char_count1`, increment its count.
        b. If the character is not in `char_count1`, add it with a count of 1.
    5. Compare the two dictionaries `char_count0` and `char_count1`:
        a. If they are equal, return `True`, indicating that the strings have the same characters.
        b. If they are not equal, return `False`, indicating that the strings have different characters.
    """
    char_count0 = {}
    char_count1 = {}

    for char in s0:
        if char in char_count0:
            char_count0[char] += 1
        else:
            char_count0[char] = 1

    for char in s1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    return char_count0 == char_count1