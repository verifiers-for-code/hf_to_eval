from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    

    Action Plan:
    1. Understand the problem requirements:
        - The function should return a list of prime factors of a given integer
        - The factors should be in ascending order
        - Each factor should appear in the list as many times as it appears in the factorization
    
    2. Initialize an empty list to store the prime factors
    
    3. Implement the factorization logic:
        - Start with the smallest prime number (2) and check if it divides the input number
        - If it does, add it to the list of prime factors and divide the input number by it
        - Repeat this process until the input number is no longer divisible by the current prime number
        - Move to the next prime number and repeat the process until the input number becomes 1
    
    4. Handle edge cases:
        - If the input number is less than or equal to 1, return an empty list
        - If the input number is a prime number, return a list containing only that number
    
    5. Return the final list of prime factors
    
    Note: Use a while loop to iterate through the prime numbers and a for loop to check divisibility.
    Be careful with the logic to ensure the correct order and count of prime factors."""
    
    if n <= 1:
        return []
    
    prime_factors = []
    divisor = 2
    
    while n > 1:
        for _ in range(n // divisor):
            prime_factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return prime_factors