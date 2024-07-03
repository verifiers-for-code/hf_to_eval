def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    
    Action Plan:
    1. Validate the input:
        - Check if the input string s is empty
        - If empty, return an empty list
    2. Split the input string s into a list of words:
        - Use the split() method to separate the string into words based on spaces
    3. Initialize an empty list to store the words with the specified number of consonants:
        - This list will store the words that meet the condition
    4. Iterate through each word in the list of words:
        - For each word, count the number of consonants:
            - Define a helper function to count consonants in a word
            - Use a loop to iterate through each character in the word
            - Check if the character is a consonant (not a vowel)
            - Increment a counter for each consonant found
        - Check if the word has exactly n consonants:
            - Compare the consonant count with n
        - If the word has exactly n consonants, add it to the list of words
    5. Return the list of words with the specified number of consonants:
        - This list will contain the words that meet the condition
    """
    if not s:
        return []
    
    def count_consonants(word):
        """Helper function to count consonants in a word"""
        vowels = "aeiouAEIOU"
        count = 0
        for char in word:
            if char.isalpha() and char not in vowels:
                count += 1
        return count
    
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result