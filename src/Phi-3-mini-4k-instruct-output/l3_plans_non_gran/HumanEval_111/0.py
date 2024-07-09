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

    

    Action Plan:
    1. Initialize an empty dictionary to store the letter counts.
    2. Split the input string into a list of individual letters.
    3. Iterate through each letter in the list:
        a. Check if the letter is already in the dictionary.
        b. If the letter is in the dictionary:
            - Increment its count by 1.
        c. If the letter is not in the dictionary:
            - Add the letter to the dictionary with a count of 1.
    4. Find the maximum count among the letter counts.
    5. Create a new dictionary containing only the letters with the maximum count.
    6. Return the new dictionary containing the letter counts.
    
    Note: Use the dictionary's built-in methods for counting and checking existence.
    Consider how to handle cases where multiple letters have the same maximum count."""

    letter_counts = {}
    for letter in test.split():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    max_count = max(letter_counts.values())
    result = {letter: count for letter, count in letter_counts.items() if count == max_count}

    return result