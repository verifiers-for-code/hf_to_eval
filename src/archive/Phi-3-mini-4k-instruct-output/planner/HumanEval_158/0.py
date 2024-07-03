def count_unique_chars(word):
    """Helper function to count the number of unique characters in a word.
    
    Args:
    word (str): The input word.
    
    Returns:
    int: The number of unique characters in the word.
    """
    return len(set(word))

def find_max(words):
    """Function to find the word with maximum number of unique characters.
    If multiple words have the same maximum number of unique characters,
    return the one which comes first in lexicographical order.
    
    Args:
    words (list): A list of strings.
    
    Returns:
    str: The word with the maximum number of unique characters.
    
    Examples:
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    """
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