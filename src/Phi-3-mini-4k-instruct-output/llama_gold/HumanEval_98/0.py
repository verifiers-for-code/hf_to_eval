def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    

    Action Plan:
    1. Define a set of uppercase vowels ("A", "E", "I", "O", "U").
    2. Initialize a counter variable to store the count of uppercase vowels.
    3. Iterate through the input string, considering only even indices (0, 2, 4, ...):
       a. Check if the character at the current index is in the uppercase vowel set.
       b. If it is, increment the counter.
    4. Return the count of uppercase vowels found at even indices."""
    
    # Step 1: Define a set of uppercase vowels
    uppercase_vowels = set("AEIOU")
    
    # Step 2: Initialize a counter variable
    count = 0
    
    # Step 3: Iterate through the input string, considering only even indices
    for i in range(0, len(s), 2):
        # Check if the character at the current index is in the uppercase vowel set
        if s[i] in uppercase_vowels:
            # Increment the counter
            count += 1
    
    # Step 4: Return the count of uppercase vowels found at even indices
    return count