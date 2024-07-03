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
    1. Split the input sentence into a list of words.
    2. Create a helper function to check if a number is prime:
       - Handle edge cases (1 is not prime, 2 is prime)
       - For numbers > 2, check if they're divisible by any number from 2 to sqrt(n)
    3. Initialize an empty list to store words with prime lengths.
    4. Iterate through each word in the split sentence:
       - Check if the length of the word is prime using the helper function
       - If prime, append the word to the list of prime-length words
    5. Join the list of prime-length words with spaces.
    6. Return the resulting string.
    """

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)