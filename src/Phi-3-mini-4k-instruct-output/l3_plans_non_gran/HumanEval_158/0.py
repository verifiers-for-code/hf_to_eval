def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    

    Action Plan:
    1. Initialize two variables: `max_word` to store the word with the maximum number of unique characters, and `max_unique_chars` to store the maximum count of unique characters.
    2. Set both `max_word` and `max_unique_chars` to `None` or a default value.
    3. Iterate through each word in the input list:
        a. Convert the current word to a set to get its unique characters.
        b. Count the number of unique characters in the word.
        c. Compare the unique character count with `max_unique_chars`.
        d. If the current word has more unique characters, update `max_word` and `max_unique_chars` with the current word and its unique character count.
    4. After iterating through all words, return `max_word` as the result.
    
    Note: Use a set to efficiently count unique characters in each word.
    Be careful when comparing and updating the maximum word and its unique characters."""

    max_word = None
    max_unique_chars = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < max_word):
            max_word = word
            max_unique_chars = unique_chars

    return max_word