from typing import List
import math

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
    

    1. Initialize an empty list to store the prime factors
       - This list will hold the prime factors of the input number
    
    2. Start a loop from 2 (the smallest prime number) and go up to the square root of the input number
       - Use a while loop to iterate through this range
    
    3. Inside the loop, check if the input number is divisible by the current iteration value
       - Use the modulo operator (%) to check for divisibility
    
    4. If the input number is divisible, add the current iteration value to the prime factors list
       - This value is a prime factor of the input number
    
    5. Divide the input number by the current iteration value
       - This reduces the input number for the next iteration
    
    6. Continue the loop until the input number is no longer divisible by the current iteration value
       - This ensures that all prime factors are found
    
    7. After the loop, check if the input number is greater than 1
       - If true, add the input number to the prime factors list
       - This is the largest prime factor of the input number
    
    8. Return the prime factors list
       - This list contains the prime factors of the input number in the order from smallest to largest
    
    Additional implementation details:
    - Use a while loop to iterate through the range of possible prime factors
    - Use the modulo operator (%) to check for divisibility
    - Use the floor division operator (//) to divide the input number by the current iteration value
    - Ensure that the function handles input numbers less than or equal to 1 correctly
    - Consider using a more efficient algorithm for larger input numbers"""
    
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    return factors