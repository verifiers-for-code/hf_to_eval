def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest prime factor
    largest_prime = -1

    # Divide n by 2 until it is odd
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        largest_prime = n

    return largest_prime