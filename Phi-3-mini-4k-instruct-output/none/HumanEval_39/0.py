
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


    def prime_fib(n: int) -> int:
        """
        prime_fib returns n-th number that is a Fibonacci number and it's also prime.
        """
        a, b = 0, 1
        count = 0
        while True:
            a, b = b, a + b
            if is_prime(a):
                count += 1
                if count == n:
                    return a