def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # Define a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Split the string into words
    words = s.split()
    
    # Initialize an empty list to store the words with n consonants
    result = []
    
    # Iterate over each word in the list
    for word in words:
        # Initialize a counter for consonants
        consonant_count = 0
        
        # Iterate over each character in the word
        for char in word:
            # Check if the character is a consonant
            if char.lower() not in vowels and char.isalpha():
                # Increment the consonant count
                consonant_count += 1
        
        # Check if the word has exactly n consonants
        if consonant_count == n:
            # Add the word to the result list
            result.append(word)
    
    # Return the result list
    return result