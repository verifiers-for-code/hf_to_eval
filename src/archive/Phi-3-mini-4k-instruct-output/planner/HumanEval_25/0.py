from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
    n (int): The integer to be factorized.
    
    Returns:
    List[int]: A list of prime factors of the input integer in ascending order.
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Step 2: Initialize an empty list to store the prime factors
    prime_factors = []
    
    # Step 3: Implement the factorization logic
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor
        if count > 0:
            prime_factors.extend([divisor] * count)
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                prime_factors.append(n)
                break
    
    # Step 4: Handle edge cases
    if not prime_factors:
        return []
    
    # Step 5: Return the final list of prime factors
    return prime_factors