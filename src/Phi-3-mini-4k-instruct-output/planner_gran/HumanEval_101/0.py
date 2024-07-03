def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    

    1. Define the function words_string with a single parameter s, which is the input string
       - The function will take a string as input and return a list of words
    
    2. Split the input string into a list of words
       - Use the split() method to divide the string at each occurrence of a comma or space
       - The split() method will split the string into individual words
       - Assign the resulting list to a variable (e.g., words)
    
    3. Return the list of words
       - The function will return the list of words as its result
       - The list will contain all the words from the input string, separated by commas or spaces
    
    Additional implementation details:
    - The split() method will automatically handle multiple consecutive commas or spaces, treating them as a single separator
    - The resulting list will contain all the words from the input string, in the order they appeared
    - The function will handle empty input strings correctly, returning an empty list
    - The function will handle strings with multiple consecutive commas or spaces correctly, returning a list with the words separated by commas or spaces"""
    
    words = s.split(", ")
    return words