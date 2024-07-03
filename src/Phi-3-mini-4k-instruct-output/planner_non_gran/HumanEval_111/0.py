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
    2. Iterate through each character in the input string:
        a. If the character is a lowercase letter, increment its count in the dictionary.
        b. If the character is not a lowercase letter, ignore it.
    3. Find the maximum count among all letter counts.
    4. Create a new dictionary to store the result:
        a. Iterate through the original dictionary:
            i. If the count of a letter is equal to the maximum count, add it to the result dictionary.
    5. Return the result dictionary.
    
    Note: Consider using a dictionary comprehension to create the result dictionary.
    Be careful when handling the case of multiple letters with the same maximum count."""
    
    letter_counts = {}
    for char in test:
        if char.islower():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    max_count = max(letter_counts.values()) if letter_counts else 0
    
    result = {letter: count for letter, count in letter_counts.items() if count == max_count}
    
    return result