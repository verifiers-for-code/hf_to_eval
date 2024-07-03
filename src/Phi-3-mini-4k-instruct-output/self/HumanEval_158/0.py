def find_max(words):
    """
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    

    Action Plan:
    1. Define a helper function to calculate unique characters count in a string
       - Use a set to count unique characters
       - Compare lengths to determine the unique count
    
    2. Use the helper function to evaluate each word in the input list
       - Maintain a running maximum count and corresponding word
    
    3. Edge cases to consider:
       - Empty input list
       - Case sensitivity
       - Non-string elements in the list
    
    4. Tie-breaking logic:
       - Keep the original word in case of a tie, based on the lexicographical order
    
    5. Return the word with the maximum number of unique characters, considering tie-breaking logic
    """
    def unique_chars_count(word):
        return len(set(word))

    if not words:
        return ""

    max_word = words[0]
    max_count = unique_chars_count(max_word)

    for word in words:
        if not isinstance(word, str):
            continue
        count = unique_chars_count(word)
        if count > max_count or (count == max_count and word < max_word):
            max_word = word
            max_count = count

    return max_word