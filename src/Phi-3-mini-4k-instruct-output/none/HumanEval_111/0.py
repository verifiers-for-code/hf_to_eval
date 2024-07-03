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
    # Split the string into a list of letters
    letters = test.split()

    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Iterate through the list of letters
    for letter in letters:
        # If the letter is already in the dictionary, increment its count
        if letter in letter_count:
            letter_count[letter] += 1
        # Otherwise, add the letter to the dictionary with a count of 1
        else:
            letter_count[letter] = 1

    # Find the maximum count of any letter
    max_count = max(letter_count.values())

    # Create a new dictionary to store the letters with the maximum count
    max_letters = {}

    # Iterate through the letter count dictionary
    for letter, count in letter_count.items():
        # If the count is equal to the maximum count, add the letter to the max_letters dictionary
        if count == max_count:
            max_letters[letter] = count

    # Return the dictionary of letters with the maximum count
    return max_letters