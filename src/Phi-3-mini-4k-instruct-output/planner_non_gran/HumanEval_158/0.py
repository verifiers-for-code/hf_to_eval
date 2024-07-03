def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    

    Action Plan:
    1. Define a helper function `count_unique_chars` to count the number of unique characters in a word:
        a. Convert the word to a set to remove duplicates
        b. Return the length of the set
    
    2. Define the main function `find_max` to find the word with maximum unique characters:
        a. Initialize variables to store the maximum unique characters count and the corresponding word
        b. Iterate through each word in the input list:
            i. Calculate the number of unique characters in the current word using the helper function
            ii. If the current word has more unique characters than the current maximum, update the maximum count and word
            iii. If the current word has the same number of unique characters as the current maximum, compare their lexicographical order
                - If the current word comes first, update the maximum count and word
        c. Return the word with the maximum unique characters
    
    3. Consider the case where multiple words have the same maximum number of unique characters:
        a. In this case, return the word that comes first in lexicographical order
    
    4. Return the final result, which is the word with the maximum number of unique characters"""
    
    def count_unique_chars(word):
        return len(set(word))
    
    max_unique_chars = 0
    max_word = ""
    
    for word in words:
        unique_chars = count_unique_chars(word)
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars:
            if word < max_word:
                max_word = word
    
    return max_word