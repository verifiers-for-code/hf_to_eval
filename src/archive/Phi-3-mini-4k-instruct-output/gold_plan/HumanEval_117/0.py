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
    1. Initialize an empty list to store the result.
    2. Split the input string 's' into individual words.
    3. Define a set of vowels (a, e, i, o, u) to identify consonants.
    4. Iterate through each word in the split string:
       a. Initialize a consonant counter for the current word.
       b. Iterate through each character in the word:
          - If the lowercase version of the character is not in the vowel set, increment the consonant counter.
       c. After counting consonants, check if the count equals the input 'n'.
       d. If the count matches 'n', append the word to the result list.
    5. Return the result list containing words with exactly 'n' consonants.
    """
    vowels = set("aeiou")
    result = []

    words = s.split()

    for word in words:
        consonant_count = 0
        for char in word.lower():
            if char not in vowels:
                consonant_count += 1

        if consonant_count == n:
            result.append(word)

    return result