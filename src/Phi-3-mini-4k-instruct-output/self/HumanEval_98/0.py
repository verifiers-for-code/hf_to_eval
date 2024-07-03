def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    

    Action Plan:
    1. Create a list of uppercase vowels
        - Include 'A', 'E', 'I', 'O', and 'U'
    2. Iterate over the string using a loop with a step of 2 to focus on even indices
    
    3. Inside the loop:
        a. Check if the index is even
        b. Check if the character at the current index is in the list of uppercase vowels
    
    4. If both conditions are met, increment a counter
    
    5. Return the counter after iterating through the entire string
    6. Edge cases:
        - Handle strings with odd length (none of the last character will be counted)
    
    7. Testing:
        - Use the provided examples to validate the function's correctness and robustness."""
    
    # Step 1: Create a list of uppercase vowels
    uppercase_vowels = ['A', 'E', 'I', 'O', 'U']
    
    # Step 2: Initialize a counter
    count = 0
    
    # Step 3: Iterate over the string using a loop with a step of 2
    for i in range(0, len(s), 2):
        # Step 3a: Check if the index is even
        if i % 2 == 0:
            # Step 3b: Check if the character at the current index is in the list of uppercase vowels
            if s[i] in uppercase_vowels:
                # Step 4: Increment the counter
                count += 1
    
    # Step 5: Return the counter
    return count