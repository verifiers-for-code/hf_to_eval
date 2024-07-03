def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    

    1. Initialize the input number (n) and a variable to store the largest prime factor (largest_prime_factor)
       - Set the initial value of largest_prime_factor to None
    
    2. Find the smallest prime factor of n:
       - Start from 2 and increment by 1
       - Check if n is divisible by the current number
       - If divisible, set largest_prime_factor to the current number and divide n by the current number
       - Repeat until n is no longer divisible by the current number
    
    3. Iterate through possible divisors:
       - Start from the smallest prime factor found in step 2
       - Increment by 2 (since all prime factors are even except for 2)
       - Continue until the square root of n (inclusive)
    
    4. Check for prime factors:
       - For each divisor, check if n is divisible by the divisor
       - If divisible, set largest_prime_factor to the divisor and divide n by the divisor
       - Repeat until n is no longer divisible by the divisor
    
    5. Return the largest prime factor:
       - If largest_prime_factor is still None, return the input number (n)
       - Otherwise, return the largest_prime_factor
    
    Additional implementation details:
    - Use a while loop to iterate through possible divisors
    - Use the modulus operator (%) to check for divisibility
    - Use the floor division operator (//) to divide n by the divisor
    - Consider using a more efficient algorithm for larger input numbers"""
    largest_prime_factor = None
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            largest_prime_factor = divisor
            n //= divisor
        else:
            divisor += 1
    if n > 1:
        largest_prime_factor = n
    return largest_prime_factor