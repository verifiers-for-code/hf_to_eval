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
    1. Split the input sentence into a list of words using the `split()` method.
    2. Define a helper function `is_prime(n)` to check if a number `n` is prime:
        a. Handle edge cases (e.g., `n` less than 2)
        b. Iterate from 2 to the square root of `n` and check for divisibility
        c. Return `True` if `n` is prime, `False` otherwise
    3. Initialize an empty string `result` to store the words with prime lengths.
    4. Iterate through each word in the list of words:
        a. Check if the length of the word is prime using the `is_prime()` function
        b. If the length is prime, add the word to the `result` string with a space separator
    5. Return the `result` string, which contains the words with prime lengths in the original order.
    
    Note: Be careful with the implementation of the `is_prime()` function to ensure it correctly identifies prime numbers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    result = ' '.join([word for word in words if is_prime(len(word))])
    return result