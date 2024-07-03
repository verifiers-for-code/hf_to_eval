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
    1. Split the string into a list of sentences, taking into account punctuation marks that delimit sentences (e.g., '.', '?', '!')
    2. Iterate through each sentence
        a. Split the sentence into individual words
        b. Check if the first word in the sentence is "I"
            - If yes, increment a counter (boredom count)
    3. Return the counter after iterating through all sentences
    4. Handle edge cases:
        - Ensure that sentences starting with a number followed by a space are considered valid
        - Include cases for punctuation (e.g., "I." or "I!") at the beginning of the sentence
    
    5. Optimization consideration:
        - Utilize built-in string methods for splitting and checking to improve performance
    """
    # Split the string into a list of sentences
    sentences = re.split(r'[.?!]', S)
    
    # Initialize boredom count
    boredom_count = 0
    
    # Iterate through each sentence
    for sentence in sentences:
        # Split the sentence into individual words
        words = sentence.strip().split()
        
        # Check if the first word in the sentence is "I"
        if words and words[0].lower() == "i":
            # Increment the boredom count
            boredom_count += 1
    
    # Return the boredom count
    return boredom_count