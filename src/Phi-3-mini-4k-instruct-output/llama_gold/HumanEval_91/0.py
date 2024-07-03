import re

def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    

    Action Plan:
    1. Import a module that allows you to split the input string into sentences based on delimiters (. , ? , !).
    2. Split the input string into a list of sentences using the delimiters.
    3. Initialize a counter to store the number of boredom sentences.
    4. Iterate through each sentence in the list:
       a. Check if the sentence starts with "I " (note the space after "I").
       b. If it does, increment the counter.
    5. Return the counter value, which represents the number of boredom sentences."""
    
    # Step 1: Import the re module for regular expressions
    import re
    
    # Step 2: Split the input string into a list of sentences using the delimiters
    sentences = re.split(r'[.?!]', S)
    
    # Step 3: Initialize a counter to store the number of boredom sentences
    boredom_count = 0
    
    # Step 4: Iterate through each sentence in the list
    for sentence in sentences:
        # Step 4a: Check if the sentence starts with "I " (note the space after "I")
        if sentence.strip().startswith("I "):
            # Step 4b: Increment the counter
            boredom_count += 1
    
    # Step 5: Return the counter value
    return boredom_count