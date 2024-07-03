def is_bored(S):
    """
    Counts the number of boredoms in a given string of words. A boredom is defined as a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    Parameters:
    S (str): A string of words.
    
    Returns:
    int: The number of boredoms in the input string.
    
    Example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Step 2: Split the input string into a list of sentences
    sentences = S.split('.')
    sentences = [sentence.strip() for sentence in sentences]
    sentences = [sentence + '.' for sentence in sentences if sentence]
    sentences = [sentence.split('?') for sentence in sentences]
    sentences = [sentence for sublist in sentences for sentence in sublist]
    sentences = [sentence.split('!') for sentence in sentences]
    sentences = [sentence for sublist in sentences for sentence in sublist]
    
    # Step 3: Initialize a variable to count boredoms
    boredoms = 0
    
    # Step 4: Iterate through each sentence
    for sentence in sentences:
        # Step 4a: Check if the sentence starts with "I" (case-insensitive)
        if sentence.lower().startswith('i'):
            # Step 4b: Increment the boredoms count
            boredoms += 1
    
    # Step 5: Return the final count of boredoms
    return boredoms