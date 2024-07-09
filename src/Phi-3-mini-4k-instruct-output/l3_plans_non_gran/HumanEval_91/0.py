def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    Action Plan:
    1. Initialize a variable to store the count of boredoms (set to 0).
    2. Split the input string into a list of sentences using a suitable delimiter (e.g., '.', '?', '!').
    3. Iterate through each sentence in the list:
        a. Check if the sentence starts with the word "I" (case-sensitive).
        b. If the sentence starts with "I", increment the boredom count.
    4. After processing all sentences, return the total count of boredoms.
    
    Note: Be mindful of punctuation marks when splitting the input string into sentences.
    Use a suitable method to check if a sentence starts with the word "I"."""
    
    boredom_count = 0
    sentences = re.split(r'[.?!]', S)
    
    for sentence in sentences:
        if sentence.strip().startswith('I'):
            boredom_count += 1
    
    return boredom_count