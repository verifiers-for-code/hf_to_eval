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
    
    3. Return the result as an array of words
    """
    # Step 1: Normalize the input string
    s = s.strip()  # Remove whitespace at the beginning and end
    s = ' '.join(s.split())  # Replace multiple spaces with a single space
    s = s.replace(',', ' ')  # Replace commas with spaces

    # Step 2: Split the normalized string into words
    words = s.split()

    # Step 3: Return the result as an array of words
    return words