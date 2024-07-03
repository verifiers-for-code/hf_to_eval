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
    1. Initialize an empty dictionary to store the result.
    2. Split the input string into a list of individual letters.
    3. Handle the case of an empty string by returning an empty dictionary.
    4. Count the occurrences of each letter in the list.
    5. Find the maximum count among all letters.
    6. Create a dictionary with all letters that have the maximum count.
    7. Return the resulting dictionary.

    """
    result = {}
    letters = test.split()

    if not letters:
        return result

    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    max_count = max(letter_counts.values())

    for letter, count in letter_counts.items():
        if count == max_count:
            result[letter] = count

    return result