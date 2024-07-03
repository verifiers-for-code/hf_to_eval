def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    

    Action Plan:
    1. Check if the input string is empty, and if so, return an empty list.
    2. Initialize an empty list to build the modified string.
    3. Iterate through each character in the input string:
       a. If the character is a comma, append a space to the list.
       b. Otherwise, append the original character to the list.
    4. Join the characters in the list into a single string.
    5. Split the resulting string into a list of words using a space as the separator.
    6. Return the list of words.
    """
    if not s:
        return []
    
    modified_string = []
    for char in s:
        if char == ',':
            modified_string.append(' ')
        else:
            modified_string.append(char)
    
    modified_string = ''.join(modified_string)
    words = modified_string.split()
    
    return words