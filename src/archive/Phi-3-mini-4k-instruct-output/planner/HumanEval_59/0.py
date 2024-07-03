def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2

    Action Plan:
    1. Understand the problem: Find the largest prime factor of a given number n, assuming n > 1 and is not a prime number.
    2. Initialize a variable to store the largest prime factor, set it to 1 (or any non-prime number).
    3. Implement a loop to find the largest prime factor:
        a. Start with the smallest prime number (2) and increment it until it exceeds the square root of n.
        b. For each prime number, check if it is a factor of n.
        c. If it is a factor, divide n by the prime number and update the largest prime factor.
        d. Repeat this process until n becomes 1 or a prime number.
    4. Handle the case when n is a prime number:
        a. If n is a prime number, return n as the largest prime factor.
    5. Return the final result: the largest prime factor of n.

    Note: Use a while loop to iterate until n becomes 1 or a prime number.
    Be careful when handling the case when n is a prime number.
    """
    largest_prime = 1
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            largest_prime = divisor
            n //= divisor
        divisor += 1

    if n > 1:
        largest_prime = n

    return largest_prime