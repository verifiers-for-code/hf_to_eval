def count_consonants(word):
    """Helper function to count consonants in a given word."""
    consonants = set('bcdfghjklmnpqrstvwxyz')
    count = 0
    for char in word.lower():
        if char in consonants:
            count += 1
    return count

def select_words(s, n):
    """Returns a list of all words from string s that contain exactly n consonants."""
    if not s:  # Handle empty string case
        return []
    
    words = s.split()  # Split the string into words
    matching_words = []  # Initialize an empty list to store matching words
    
    for word in words:
        consonant_count = count_consonants(word)  # Count consonants in the current word
        if consonant_count == n:  # Check if the consonant count equals n
            matching_words.append(word)  # Append the word to the list of matching words
    
    return matching_words