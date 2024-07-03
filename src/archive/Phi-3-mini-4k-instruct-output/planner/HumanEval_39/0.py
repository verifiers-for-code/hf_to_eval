import math

def is_prime(num: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """
    Generate the n-th Fibonacci number.
    
    Args:
    n (int): The position in the Fibonacci sequence.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def prime_fib(n: int) -> int:
    """
    Return the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position in the sequence of prime Fibonacci numbers.
    
    Returns:
    int: The n-th prime Fibonacci number.
    
    Raises:
    ValueError: If n is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("n must be greater than 0.")
    
    counter = 0
    i = 1
    while counter < n:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            counter += 1
        i += 1
    
    return fib_num