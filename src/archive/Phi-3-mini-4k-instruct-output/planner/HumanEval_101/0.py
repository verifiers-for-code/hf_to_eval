def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
    Action Plan:
    1. Define the function `words_string` that takes a string `s` as input.
    2. Initialize an empty list `words` to store the individual words.
    3. Split the input string `s` into a list of words using the `split()` method.
    4. Iterate through each word in the list of words:
        a. Check if the word contains a comma (',') or a space (' ').
        b. If a separator is found, split the word into sub-words using the `split()` method.
        c. Add the sub-words to the `words` list.
    5. Return the `words` list containing all the individual words.
    
    Note: The `split()` method can handle both commas and spaces as separators, so no additional logic is needed for this.
    """
    words = s.split()
    for i, word in enumerate(words):
        if ',' in word or ' ' in word:
            words[i] = word.split(',') if ',' in word else word.split(' ')
    return words