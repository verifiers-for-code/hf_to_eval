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
    1. Define a set of vowels (e.g., 'a', 'e', 'i', 'o', 'u') for consonant counting.
    2. Split the input string into a list of words using a suitable method (e.g., `split()`).
    3. Initialize an empty list to store the words that meet the condition.
    4. Iterate through each word in the list of words:
        a. Convert the word to lowercase for case-insensitive comparison.
        b. Count the number of consonants in the word:
            - Iterate through each character in the word.
            - Check if the character is an alphabet letter (not a vowel and not a space).
            - Increment the consonant count if the character is a consonant.
        c. Check if the word contains exactly n consonants.
        d. If the condition is met, add the word to the result list.
    5. Return the list of words that meet the condition."""

    vowels = set('aeiou')
    words = s.split()
    result = []

    for word in words:
        word_lower = word.lower()
        consonant_count = sum(1 for char in word_lower if char.isalpha() and char not in vowels)
        if consonant_count == n:
            result.append(word)

    return result