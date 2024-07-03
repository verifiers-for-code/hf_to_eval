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
    # Step 1: Split the string into a list of sentences
    sentences = [sentence.strip() for sentence in re.split('[.!?]', S) if sentence.strip()]
    
    # Step 2: Iterate through each sentence
    boredom_count = 0
    for sentence in sentences:
        # Step 2a: Split the sentence into individual words
        words = sentence.split()
        
        # Step 2b: Check if the first word in the sentence is "I"
        if words and words[0].lower() == "i":
            # Step 3: Increment the boredom count
            boredom_count += 1
            
    # Step 4: Handle edge cases
    # Sentences starting with a number followed by a space are considered valid
    # Include cases for punctuation (e.g., "I." or "I!") at the beginning of the sentence
    # This is already handled in the code above
    
    # Step 5: Return the boredom count
    return boredom_count