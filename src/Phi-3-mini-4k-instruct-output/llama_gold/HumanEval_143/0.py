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
    1. Split the input sentence into a list of words using a space as the separator.
    2. Initialize an empty list to store words with prime lengths.
    3. Iterate through each word in the list:
       a. Initialize a flag to track if the word length is prime.
       b. Check if the word length is 1 (considered prime) or 2 (even prime).
       c. If not, iterate from 2 to the word length to check for divisors:
          - If a divisor is found, set the flag to indicate the length is not prime.
       d. If the flag is still unset (i.e., the length is prime), add the word to the result list.
    4. Join the words in the result list into a new string with spaces in between.
    5. Return the resulting string containing words with prime lengths.
    """
    words = sentence.split()
    prime_words = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)