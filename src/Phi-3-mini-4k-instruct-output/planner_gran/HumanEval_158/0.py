def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    

    1. Initialize variables to store the maximum number of unique characters and the corresponding word
       - Set max_unique_chars to 0 and max_word to an empty string
    
    2. Iterate through each word in the input list:
       a. Count the number of unique characters in the current word
          - Convert the word to a set to remove duplicates
          - Use the len() function to get the number of unique characters
       b. Check if the current word has more unique characters than the previous maximum
          - Compare the count of unique characters with max_unique_chars
          - If it's greater, update max_unique_chars and max_word
    
    3. After iterating through all words, return the word with the maximum number of unique characters
       - max_word will hold the word with the maximum number of unique characters
    
    Additional implementation details:
    - Use a loop to iterate through the list of words
    - Use a set to count unique characters in each word
    - Use the len() function to get the number of unique characters
    - Update max_word and max_unique_chars accordingly
    - Return the max_word at the end
    - Handle cases with multiple words having the same maximum number of unique characters"""

    max_unique_chars = 0
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars:
            if word < max_word:
                max_word = word

    return max_word