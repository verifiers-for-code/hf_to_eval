import math

def is_prime(n):
    """Check if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """Return a string containing words from the input sentence whose lengths are prime numbers.
    
    Args:
    sentence (str): The input sentence.
    
    Returns:
    str: A string containing words with prime lengths from the input sentence.
    
    Example:
        words_in_sentence("This is a test") -> "is"
        words_in_sentence("lets go for swimming") -> "go for"
    """
    words = sentence.split()
    result = ' '.join([word for word in words if is_prime(len(word))])
    return result