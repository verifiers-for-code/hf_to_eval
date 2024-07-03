import re

def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    1. Initialize a counter variable to store the number of boredoms
       - Set the counter to 0 initially
    
    2. Split the input string into a list of sentences
       - Use a regular expression to split the string into sentences, considering '.', '?', and '!' as delimiters
       - Store the list of sentences in a variable (e.g., sentences)
    
    3. Iterate through each sentence in the list of sentences:
       a. Check if the sentence starts with the word "I" (case-insensitive)
       b. If the sentence starts with "I":
          - Increment the boredom counter by 1
    
    4. Return the final count of boredoms
    
    Additional implementation details:
    - Use the `re` module for regular expression operations
    - Use the `split()` method to split the string into sentences
    - Use the `startswith()` method to check if a sentence starts with "I"
    - Ensure that the function handles empty input strings correctly
    - Consider using a more efficient approach for splitting sentences, such as using `re.split()` with a pattern that matches sentence delimiters
    """
    boredom_count = 0
    sentences = re.split(r'[.?!]\s*', S)
    for sentence in sentences:
        if sentence.strip().lower().startswith('i'):
            boredom_count += 1
    return boredom_count