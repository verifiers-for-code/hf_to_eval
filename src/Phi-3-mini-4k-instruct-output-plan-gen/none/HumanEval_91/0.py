
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
    # Split the string into sentences using regex
    sentences = re.split('[.!?]', S)

    # Initialize a counter for boredoms
    boredoms = 0

    # Iterate through each sentence
    for sentence in sentences:
        # Strip leading and trailing whitespaces
        sentence = sentence.strip()

        # Check if the sentence starts with "I"
        if sentence.startswith('I'):
            boredoms += 1

    return boredoms