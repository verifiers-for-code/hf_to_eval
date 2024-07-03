def prime_length(string):
    """
    Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise.

    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False

    Action Plan:
    1. Define a function `prime_length` that takes a string as input.
    2. Initialize a variable to store the length of the input string.
    3. Implement a helper function `is_prime` to check if a number is prime:
        a. Take an integer as input.
        b. Check if the number is less than 2 (not prime).
        c. Iterate from 2 to the square root of the number:
            - If the number is divisible by any of these values, it's not prime.
        d. If the number is not divisible by any of these values, it's prime.
    4. Use the `is_prime` function to check if the length of the input string is prime.
    5. Return `True` if the length is prime, `False` otherwise.
    6. Consider adding a docstring to explain the function's purpose, parameters, and return value.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return is_prime(len(string))