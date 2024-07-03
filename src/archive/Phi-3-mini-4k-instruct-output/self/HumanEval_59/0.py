def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
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
    # Since we're dividing n by its prime factors, the last prime factor checked
    # will be the largest prime factor if n is not a prime number
    # Validate if the resulting prime factor is actually the largest
    if n == 1:
        return prime_factor
    else:
        return "Error: n is a prime number or the largest prime factor is not found."