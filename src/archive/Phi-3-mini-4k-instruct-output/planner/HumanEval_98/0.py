def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
    Action Plan:
    1. Initialize a variable to store the count of uppercase vowels in even indices.
    2. Iterate through the input string, considering each character and its index.
    3. For each character, check if it is an uppercase vowel (A, E, I, O, U).
    4. If the character is an uppercase vowel, check if its index is even (using the modulo operator).
    5. If the index is even, increment the count variable.
    6. After iterating through the entire string, return the final count of uppercase vowels in even indices.
    
    Note: Use the `isupper()` method to check if a character is uppercase, and the `in` operator to check if a character is a vowel.
    Be careful when checking for even indices, as the index starts from 0.
    """
    count = 0
    vowels = 'AEIOU'
    for i, char in enumerate(s):
        if char.isupper() and char in vowels and i % 2 == 0:
            count += 1
    return count