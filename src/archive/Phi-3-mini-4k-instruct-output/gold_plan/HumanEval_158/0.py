def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb", "cc"]) == ""aaaaaaa"

    Action Plan:
    1. Understand the input:
       - 'words' is a list of strings

    2. For each word in the list:
       a. Count the number of unique characters
          Hint: Consider using a set to get unique characters

    3. Determine the maximum number of unique characters among all words

    4. Create a list of words that have the maximum number of unique characters

    5. If there are multiple words with the same maximum number of unique characters:
       a. Sort these words lexicographically (alphabetically)

    6. Return the first word from the sorted list of words with maximum unique characters

    Note: Consider using a sorting function with a custom key that takes into account
    both the number of unique characters (in descending order) and the lexicographical
    order of the words.
    """
    max_unique_chars = 0
    max_unique_words = []

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_unique_words = [word]
        elif unique_chars == max_unique_chars:
            max_unique_words.append(word)

    max_unique_words.sort()
    return max_unique_words[0]