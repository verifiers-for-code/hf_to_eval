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
    """
    # Step 2: Split the input string S into sentences
    sentences = re.split(r'[.!?]\s*', S)
    
    # Step 3: Initialize a counter for boredoms
    boredoms = 0
    
    # Step 4: Iterate through the list of sentences
    boredoms = sum(1 for sentence in sentences if sentence.strip().startswith('I '))
    
    # Step 5: Return the final count of boredoms
    return boredoms