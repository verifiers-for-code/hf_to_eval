def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    Parameters:
    S (str): A string containing sentences separated by '.', '?' or '!'.
    
    Returns:
    int: The number of sentences that start with the word "I".
    
    Action Plan:
    1. Define a function `is_bored` that takes a string `S` as input.
    2. Split the input string `S` into a list of sentences using the `split` method, with delimiters '.', '?' or '!'.
    3. Initialize a variable `boredoms` to 0 to count the number of boredoms.
    4. Iterate through each sentence in the list of sentences:
        a. Check if the sentence starts with the word "I" (case-insensitive).
        b. If the sentence starts with "I", increment the `boredoms` count by 1.
    5. After iterating through all sentences, return the final count of boredoms.
    """
    sentences = S.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    sentences = [s.split('?') for s in sentences]
    sentences = [item for sublist in sentences for item in sublist]
    sentences = [s.split('!') for s in sentences]
    sentences = [item for sublist in sentences for item in sublist]
    
    boredoms = 0
    for sentence in sentences:
        if sentence.lower().startswith('i'):
            boredoms += 1
    
    return boredoms