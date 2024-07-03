def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    Args:
    s (str): Input string

    Returns:
    str: Ordered version of the input string

    Action Plan:
    1. Define the function `anti_shuffle` that takes a string `s` as input.
    2. Split the input string `s` into a list of words using the `split()` method.
    3. Initialize an empty list `ordered_words` to store the ordered versions of each word.
    4. Iterate through each word in the list of words:
        a. Convert the word to a list of characters.
        b. Sort the list of characters in ascending order based on ASCII values.
        c. Join the sorted characters back into a string.
        d. Add the ordered word to the `ordered_words` list.
    5. Join the `ordered_words` list back into a string using the `join()` method, with a space as the separator.
    6. Return the final ordered string.
    """
    words = s.split()
    ordered_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        ordered_words.append(sorted_word)
    return ' '.join(ordered_words)