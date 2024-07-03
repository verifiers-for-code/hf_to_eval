def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    

    Action Plan:
    1. Normalize the input string by:
        a. Replacing multiple consecutive spaces or commas with a single space or comma.
        b. Trimming the string from whitespace at the beginning and end
    
    2. Split the normalized string into words using the split() function. Handle both comma and space delimiters.
    
    3. Return the result as an array of words"""
    
    # Normalize the input string
    s = s.replace(",", " ").replace("  ", " ").strip()
    
    # Split the normalized string into words
    words = s.split()
    
    # Return the result as an array of words
    return words