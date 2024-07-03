def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Returns a string containing words from the original sentence whose lengths are prime numbers.
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Filter words with prime length using list comprehension
    prime_length_words = [word for word in words if is_prime(len(word))]
    
    # Join the filtered words into a string, using the original spaces as separators
    result = ' '.join(prime_length_words)
    
    return result