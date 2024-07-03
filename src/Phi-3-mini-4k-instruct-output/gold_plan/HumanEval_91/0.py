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
    1. Import the 're' module for regular expressions.
    2. Use re.split() to split the input string S into sentences:
       - Create a regex pattern that matches '.', '?', or '!' followed by optional whitespace.
       - Apply this pattern to split S into a list of sentences.
    3. Initialize a counter for boredoms.
    4. Iterate through the list of sentences:
       - Check if each sentence starts with 'I ' (note the space after 'I').
       - If it does, increment the boredom counter.
    5. Return the final count of boredoms.

    Hint: Consider using a list comprehension and the 'sum' function to combine steps 3-5.
    """
    # Step 2: Split the input string into sentences
    sentences = re.split(r'[.?!]\s*', S)
    
    # Step 3: Initialize a counter for boredoms
    boredom_count = 0
    
    # Step 4: Iterate through the list of sentences
    for sentence in sentences:
        # Check if the sentence starts with 'I '
        if sentence.strip().startswith('I '):
            boredom_count += 1
    
    # Step 5: Return the final count of boredoms
    return boredom_count