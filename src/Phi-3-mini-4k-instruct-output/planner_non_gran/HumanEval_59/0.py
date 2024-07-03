def largest_prime_factor(n: int):
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
    Be careful when handling the case when n is a prime number."""
    
    # Step 2: Initialize the largest prime factor variable
    largest_prime = 1
    
    # Step 3: Implement a loop to find the largest prime factor
    # Start with the smallest prime number (2) and increment it until it exceeds the square root of n
    i = 2
    while i * i <= n:
        # Check if i is a factor of n
        if n % i == 0:
            # Update the largest prime factor
            largest_prime = i
            # Divide n by i
            n //= i
        else:
            # Increment i
            i += 1
    
    # Step 4: Handle the case when n is a prime number
    # If n is a prime number, return n as the largest prime factor
    if n > 1:
        largest_prime = n
    
    # Step 5: Return the final result
    return largest_prime