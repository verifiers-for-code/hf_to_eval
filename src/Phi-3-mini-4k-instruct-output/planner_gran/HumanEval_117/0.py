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
    
    Action Plan:
    1. Check if the input string is empty:
       - If empty, return an empty list
    
    2. Split the input string into a list of words:
       - Use the appropriate string method to split the string into individual words
    
    3. Initialize an empty list to store the result:
       - This list will hold the words with exactly n consonants
    
    4. Iterate through each word in the list of words:
       a. Initialize a counter for consonants in the current word
       b. Iterate through each character in the word:
          - Check if the character is a consonant (using a helper function or a set of consonants)
          - If consonant, increment the consonant counter
       c. Check if the consonant counter is equal to n:
          - If true, add the word to the result list
    
    5. Return the result list:
       - This list contains all words from the input string with exactly n consonants
    
    Additional implementation details:
    - Define a helper function to check if a character is a consonant (e.g., using a set of consonants)
    - Use a set or list to store the consonants for efficient lookups
    - Consider using a generator expression or list comprehension for concise code
    - Ensure the function handles edge cases, such as an empty input string or n being 0"""
    
    if not s:
        return []
    
    consonants = set("bcdfghjklmnpqrstvwxyz")
    words = s.split()
    result = [word for word in words if sum(1 for char in word if char.lower() in consonants) == n]
    
    return result