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
    

    1. Initialize variables:
       - Set `a` and `b` to 0 and 1, respectively, as the first two Fibonacci numbers
       - Set `count` to 0, which will keep track of the number of prime Fibonacci numbers found
       - Set `n` to the input number, which is the position of the desired prime Fibonacci number
    
    2. Generate Fibonacci numbers and check for primality:
       - Create a loop that continues until `count` reaches `n`
       - Inside the loop:
         a. Check if the current Fibonacci number `a` is prime using the `is_prime` function
         b. If `a` is prime, increment `count`
         c. Calculate the next Fibonacci number by adding `a` and `b`
         d. Update `a` and `b` for the next iteration
    
    3. Define the `is_prime` function:
       - This function takes an integer `n` as input and returns `True` if `n` is prime, `False` otherwise
       - Check if `n` is less than 2, in which case it's not prime
       - Iterate from 2 to the square root of `n` and check if `n` is divisible by any of these numbers
       - If `n` is divisible, return `False`; otherwise, return `True`
    
    4. Return the nth prime Fibonacci number:
       - Once the loop completes, return the value of `a`, which is the nth prime Fibonacci number
    
    Additional implementation details:
    - Use a while loop to generate Fibonacci numbers and check for primality
    - Use a for loop or conditional statements to implement the `is_prime` function
    - Ensure that the function handles edge cases, such as `n` being 0 or 1
    - Consider optimizing the `is_prime` function for better performance
    """
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    a, b = 0, 1
    count = 0
    while count < n:
        if is_prime(a):
            count += 1
        a, b = b, a + b
    return a