def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2

    Action Plan:
    1. Define a helper function `is_prime(k)` to check if a number k is prime:
       - Handle edge cases (k < 2)
       - Implement a loop to check for divisibility
       - Return True if no divisors found, False otherwise

    2. Initialize a variable to store the largest prime factor found

    3. Iterate through potential factors from 2 to n:
       - Check if the current number is a factor of n
       - If it is a factor, use the is_prime function to check if it's prime
       - If it's a prime factor, update the largest prime factor if necessary

    4. Return the largest prime factor found
    """

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True

    largest_prime = 0
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime