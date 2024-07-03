def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]

    Action Plan:
    1. Check if the input string is empty:
       - If it is, return an empty list
    
    2. Replace commas with spaces:
       - Iterate through each character in the input string
       - If the character is a comma, replace it with a space
       - Store the modified characters in a new list
    
    3. Join the modified characters:
       - Combine the list of characters into a single string
    
    4. Split the string into words:
       - Use a string method to split the modified string into a list of words
    
    5. Return the resulting list of words
    """
    if not s:
        return []
    
    s = s.replace(",", " ")
    s = "".join(s)
    words = s.split()
    
    return words