def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    

    Action Plan:
    1. Define the function `words_string` that takes a string `s` as input.
    2. Split the input string `s` into a list of words using the `split` method.
    3. The `split` method will automatically handle both commas and spaces as separators.
    4. Return the list of words as the result.
    
    Note: The `split` method will return a list of strings, where each string is a word from the input string.
    No additional error handling or validation is needed, as the `split` method can handle any string input."""
    
    # Step 1: Define the function `words_string` that takes a string `s` as input.
    def words_string(s):
        # Step 2: Split the input string `s` into a list of words using the `split` method.
        words = s.split(", ")
        
        # Step 3: The `split` method will automatically handle both commas and spaces as separators.
        
        # Step 4: Return the list of words as the result.
        return words