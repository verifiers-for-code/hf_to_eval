import math

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    """
    Generate the n-th Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def prime_fib(n):
    """
    Return the n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return "Error: n must be greater than 0"
    
    count = 0
    i = 1
    while count < n:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
        i += 1
    
    return fib_num