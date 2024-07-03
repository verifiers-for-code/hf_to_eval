def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """Generate the n-th Fibonacci number using memoization."""
    fib_cache = {0: 0, 1: 1}
    def fib(n):
        if n not in fib_cache:
            fib_cache[n] = fib(n-1) + fib(n-2)
        return fib_cache[n]
    return fib(n)

def prime_fib(n: int) -> int:
    """Find the n-th Fibonacci prime number."""
    count = 0
    num = 2
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num