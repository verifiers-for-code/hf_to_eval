def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    

    Action Plan:
    1. Create a helper function to check if a number is prime:
       a. Check if the number is less than 2 (not prime).
       b. Iterate from 2 to the number-1, checking if the number is divisible by any of these values.
       c. If the number is not divisible by any of these values, it's prime.
    2. Initialize a variable to store the largest prime factor, initially set to 1.
    3. Iterate from 2 to the input number n:
       a. Check if the current number is a factor of n (n % current number == 0).
       b. If it's a factor, use the helper function to check if it's prime.
       c. If it's prime, update the largest prime factor if it's larger than the current largest.
    4. Return the largest prime factor found."""

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    largest_prime = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime