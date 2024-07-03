def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    

    Action Plan:
    1. Define the problem constraints (e.g., finding the n-th Fibonacci prime prime number).
    2. Implement a function to generate Fibonacci numbers up to a certain limit or the n-th Fibonacci number.
    3. Implement a prime-checking function that iterates over the possible divisors of a number.
    4. Use a loop or an efficient iterative process to find and return the n-th Fibonacci prime number.
    5. Ensure optimal time complexity, possibly utilizing a memoization strategy for generating Fibonacci numbers.
    6. Test and handle edge cases such as n being too large to practically find the prime Fibonacci number."""

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    count = 0
    num = 0
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num