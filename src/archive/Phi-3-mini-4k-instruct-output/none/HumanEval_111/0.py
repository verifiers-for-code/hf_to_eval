def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # Initialize an empty dictionary to store the letter counts
    letter_counts = {}
    
    # Iterate over each character in the input string
    for char in test.split():
        # If the character is already in the dictionary, increment its count
        if char in letter_counts:
            letter_counts[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            letter_counts[char] = 1
    
    # Find the maximum count in the dictionary
    max_count = max(letter_counts.values())
    
    # Filter the dictionary to only include letters with the maximum count
    result = {k: v for k, v in letter_counts.items() if v == max_count}
    
    return result