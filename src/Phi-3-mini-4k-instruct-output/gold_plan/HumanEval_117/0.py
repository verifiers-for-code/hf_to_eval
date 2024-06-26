def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    """
    result = []
    vowels = set("aeiou")

    # Split the input string into words
    words = s.split()

    for word in words:
        consonant_count = 0
        # Iterate through each character in the word
        for char in word.lower():
            # If the character is not a vowel, increment the consonant counter
            if char not in vowels:
                consonant_count += 1

        # If the consonant count matches the input 'n', append the word to the result list
        if consonant_count == n:
            result.append(word)

    return result