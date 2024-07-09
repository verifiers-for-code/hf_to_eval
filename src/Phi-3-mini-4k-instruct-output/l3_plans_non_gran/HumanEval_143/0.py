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
    2. Define a helper function `is_prime()` to check if a number is prime:
        a. Take an integer `num` as input.
        b. Check if `num` is less than 2, return `False` if true.
        c. Iterate from 2 to the square root of `num` to check for divisors.
        d. Return `True` if no divisors are found, `False` otherwise.
    3. Create a new list `prime_words` to store the words with prime-lengthed words.
    4. Iterate through each word in the list of words:
        a. Calculate the length of the current word.
        b. Check if the length is prime using the `is_prime()` function.
        c. If the length is prime, add the word to the `prime_words` list.
    5. Join the `prime_words` list into a new string using the `join()` method.
    6. Return the final string containing the words with prime-lengthed words.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)