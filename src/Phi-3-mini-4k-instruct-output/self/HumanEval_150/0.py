import math

def is_prime(n):
    """
    A helper function to check if a number is prime.
    
    Input: an integer n
    Return: boolean indicating if n is prime or not
    Implement logic that checks divisibility from 2 to sqrt(n)
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """
    A simple program which should return the value of x if n is a prime number
    and should return the value of y otherwise.
    
    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    Action Plan:
    1. Define a helper function to check if a number is prime:
        - Input: an integer n
        - Return: boolean indicating if n is prime or not
        - Implement logic that checks divisibility from 2 to sqrt(n)
    
    2. In the main function, receive the inputs n, x, and y
    
    3. Use the helper function to check if n is prime
        - If the returned value is True (n is prime), return x
        - Otherwise, return y
    
    4. Handle edge cases:
        - n == 0, 1, or negative numbers
        - n < 2, as the smallest prime number is 2
    
    5. Write test cases based on the examples provided and additional edge cases to ensure the function works as expected
    
    6. Ensure the function is efficient by avoiding unnecessary computations and optimizing the prime check function
    """
    if n <= 1 or n < 2:
        return y
    if is_prime(n):
        return x
    return y