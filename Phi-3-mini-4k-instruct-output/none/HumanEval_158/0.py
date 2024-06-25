
    def find_max(words):
        """Write a function that accepts a list of strings.
        The list contains different words. Return the word with maximum number
        of unique characters. If multiple strings have maximum number of unique
        characters, return the one which comes first in lexicographical order.

        find_max(["name", "of", "string"]) == "string"
        find_max(["name", "enam", "game"]) == "enam"
        find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
        """

        # Initialize variables
        max_unique_chars = 0
        max_unique_word = ""

        # Iterate through the list of words
        for word in words:
            # Count unique characters in the current word
            unique_chars = len(set(word))

            # Check if the current word has more unique characters than the previous max
            if unique_chars > max_unique_chars:
                max_unique_chars = unique_chars
                max_unique_word = word
            # If the current word has the same number of unique characters as the previous max,
            # check if it comes first in lexicographical order
            elif unique_chars == max_unique_chars:
                if word < max_unique_word:
                    max_unique_word = word

        return max_unique_word