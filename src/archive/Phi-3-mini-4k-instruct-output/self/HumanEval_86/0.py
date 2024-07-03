def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    :param s: Input string
    :return: Sorted string
    """
    # Step 1: Split the input string into a list of words using the `split()` method.
    words = s.split()

    # Step 2: Iterate over the list using a loop. For each word:
    # a. Convert the word into a list of characters.
    # b. Sort the list of characters in ascending order.
    # c. Join the sorted characters back into a word.
    sorted_words = [''.join(sorted(word)) for word in words]

    # Step 3: Reconstruct the final string, keeping the original order of words and spaces.
    # a. Consider if the first character needs to be capitalized for the first word.
    final_string = ' '.join(sorted_words)
    if final_string:
        final_string = final_string[0].upper() + final_string[1:]

    return final_string