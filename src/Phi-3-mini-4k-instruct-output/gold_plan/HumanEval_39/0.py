import math

def is_prime(p: int) -> bool:
    """
    Check if a number is prime.
    """
    if p < 2:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    fib_sequence = [0, 1]
    prime_fib_count = 0

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if is_prime(next_fib):
            prime_fib_count += 1
            if prime_fib_count == n:
                return next_fib