def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0

    Action Plan:
    1. Initialize a counter variable to 0.
    2. Iterate through the string s, considering only even indices:
       - Use a for loop with a step of 2 to access even indices.
    3. For each character at an even index:
       - Check if it is an uppercase vowel (A, E, I, O, or U).
       - Tip: You can use the 'in' operator to check if the character is in a string of uppercase vowels.
    4. If the character is an uppercase vowel, increment the counter.
    5. After the loop ends, return the final count.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count