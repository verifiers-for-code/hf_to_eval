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
    1. Split the input string into a list of words using spaces as separators.
    2. Initialize an empty list to store the result.
    3. Iterate through each word in the list:
       a. Initialize a counter for consonants in the current word.
       b. Iterate through each character in the word:
          - Convert the character to lowercase for comparison.
          - Check if the lowercase character is not a vowel (a, e, i, o, u).
          - If it's a consonant, increment the consonant counter.
       c. Check if the consonant count matches the given number (n).
       d. If it matches, add the word to the result list.
    4. Return the result list containing words with exactly n consonants."""

    # Step 1: Split the input string into a list of words
    words = s.split()

    # Step 2: Initialize an empty list to store the result
    result = []

    # Step 3: Iterate through each word in the list
    for word in words:
        # Step 3a: Initialize a counter for consonants in the current word
        consonant_count = 0

        # Step 3b: Iterate through each character in the word
        for char in word:
            # Convert the character to lowercase for comparison
            char = char.lower()

            # Check if the lowercase character is not a vowel
            if char not in ['a', 'e', 'i', 'o', 'u']:
                # If it's a consonant, increment the consonant counter
                consonant_count += 1

        # Step 3c: Check if the consonant count matches the given number (n)
        if consonant_count == n:
            # If it matches, add the word to the result list
            result.append(word)

    # Step 4: Return the result list containing words with exactly n consonants
    return result