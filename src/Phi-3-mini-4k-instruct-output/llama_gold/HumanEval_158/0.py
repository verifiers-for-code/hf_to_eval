def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    

    Action Plan:
    1. Initialize an empty variable to store the result word.
    2. Iterate through each word in the input list:
       a. Calculate the number of unique characters in the word.
       b. If this word has more unique characters than the current result word:
          - Update the result word to be this word.
       c. If this word has the same number of unique characters as the current result word:
          - Compare this word with the current result word in lexicographical order.
          - If this word comes first, update the result word to be this word.
    3. After processing all words, return the result word."""

    result_word = ""
    max_unique_chars = 0

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result_word = word
        elif unique_chars == max_unique_chars:
            if word < result_word:
                result_word = word

    return result_word