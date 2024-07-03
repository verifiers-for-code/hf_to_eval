import math

def is_prime(p):
    """
    Check if a number is prime.
    """
    if p < 2:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    fib_seq = [0, 1]
    while True:
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)
        if is_prime(next_fib):
            n -= 1
            if n == 0:
                return next_fib