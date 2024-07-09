import math

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """
    Generate the nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def prime_fib(n: int) -> int:
    """
    Return the nth prime Fibonacci number.
    """
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")
    count = 0
    i = 2
    while True:
        fib = fibonacci(i)
        if is_prime(fib):
            count += 1
            if count == n:
                return fib