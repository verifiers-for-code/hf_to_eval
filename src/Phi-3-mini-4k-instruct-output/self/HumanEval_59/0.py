def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    

    Action Plan:
    1. Set initial prime factor:
        - Start with 2 as the smallest prime
    
    2. Begin a loop to check for prime factors:
        - While n is greater than 1, perform the following steps
    
    3. Check divisibility and find the largest prime factor:
        - If n is divisible by the current prime factor, divide n by it
        - Once n is no longer divisible by the current prime factor, move to the next prime
    
    4. Edge cases and validation:
        - Consider the edge cases where n might not have a prime factor other than 1
        - Validate if the resulting prime factor is actually the largest
    
    5. Return the largest prime factor:
        - After exiting the loop, return the last checked prime factor"""
    
    # Step 1: Set initial prime factor
    prime_factor = 2
    
    # Step 2: Begin a loop to check for prime factors
    while n > 1:
        # Step 3: Check divisibility and find the largest prime factor
        if n % prime_factor == 0:
            n //= prime_factor
        else:
            prime_factor += 1
    
    # Step 4: Edge cases and validation
    # If n is still greater than 1, it means it is a prime number itself
    if n > 1:
        return n
    
    # Step 5: Return the largest prime factor
    return prime_factor