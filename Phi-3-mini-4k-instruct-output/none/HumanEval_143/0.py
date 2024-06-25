
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def words_in_sentence(sentence):
        """Return a string containing words from the original sentence with prime length."""
        words = sentence.split()
        prime_words = [word for word in words if is_prime(len(word))]
        return ' '.join(prime_words)