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
    1. Write a helper function `count_consonants(word)` to count consonants in a given word:
        a. Define a set of consonants
        b. Iterate through the word, incrementing a counter for consonant characters
    
    2. In the main function `select_words(s, n)`:
        a. Initialize an empty list to store matching words
        b. Split the string `s` into words using a space as a delimiter
        c. Iterate through each word in the list
            i. Call the helper function to count consonants in the current word
            ii. Check if the consonant count equals `n`
            iii. If true, append the word to the list of matching words
    
    3. Return the list of matching words
    
    4. Consider edge cases and their implications:
        a. Handle empty input string gracefully by returning an empty list
        b. Handle cases with spaces as part of the word
    
    5. Suggest using descriptive variable names and commenting to maintain readability"""
    
    # Helper function to count consonants in a word
    def count_consonants(word):
        consonants = set("bcdfghjklmnpqrstvwxyz")
        count = 0
        for char in word.lower():
            if char in consonants:
                count += 1
        return count
    
    # Main function to select words with exactly n consonants
    if not s:
        return []
    
    words = s.split()
    matching_words = []
    for word in words:
        if count_consonants(word) == n:
            matching_words.append(word)
    
    return matching_words