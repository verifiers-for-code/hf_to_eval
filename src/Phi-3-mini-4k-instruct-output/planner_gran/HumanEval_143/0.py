def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    
    1. Split the input sentence into a list of words
       - Use the appropriate string method to split the sentence into individual words
    
    2. Create an empty list to store the words with prime length
       - This list will hold the words that meet the prime length condition
    
    3. Iterate through each word in the list of words:
       a. Check if the length of the current word is prime
          - Use a helper function (is_prime) to determine if the length is prime
       b. If the length is prime:
          - Add the word to the list of words with prime length
    
    4. Create a new string with the words that have prime length
       - Use a string method to join the words with a space separator
    
    5. Return the new string with words that have prime length
    
    Additional implementation details:
    - Implement the is_prime helper function to check if a number is prime
    - Use a loop or list comprehension to iterate through the words and check their lengths
    - Use the appropriate string methods for splitting, joining, and indexing
    - Ensure that the function handles empty input strings and sentences correctly
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)