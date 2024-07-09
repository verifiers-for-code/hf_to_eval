def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    

    Action Plan:
    1. Initialize a variable to store the count of uppercase vowels in even indices.
    2. Iterate through the string, starting from the second character (index 1) and incrementing by 2.
    3. Inside the loop, check if the current character is an uppercase vowel (a, e, i, o, u).
    4. If the character is an uppercase vowel, increment the count.
    5. After the loop, return the final count of uppercase vowels in even indices.
    
    Note: Use a loop with a step size of 2 to iterate through the string with even indices.
    Be careful to only count uppercase vowels in even indices."""
    
    count = 0
    vowels = 'AEIOU'
    for i in range(1, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count