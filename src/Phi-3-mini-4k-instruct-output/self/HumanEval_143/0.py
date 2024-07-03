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
    
    Action Plan:
    1. Define a helper function `is_prime(n)`:
        a. Handle edge cases (0 and 1 are not prime)
        b. Check for divisibility from 2 up to the square root of n
        c. Return True if n is prime, else False
    
    2. In the main function `words_in_sentence(sentence)`:
        a. Split the sentence into words
        b. Use a list comprehension to filter words with prime length using `is_prime()`
        c. Join the filtered words into a string, using the original spaces as separators
    
    3. Test case scenarios:
        a. Simple sentence with one prime-length word
        b. Sentence with multiple prime-length words
        c. Sentence with no prime-length words
    
    4. Edge case considerations:
        a. Sentence with length equals to 1 or empty
        b. Sentence with numbers or special characters
    
    5. Output formatting:
        a. Return a string with filtered and original word order
    
    6. Optimization:
        a. Consider using generator expressions for memory efficiency if necessary"""

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