def prime_length(string):
    """
    Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise.
    
    Action Plan:
    1. Define the prime_length function that takes a string as input.
    2. Create a helper function is_prime to check if a number is prime:
        a. Handle edge cases (numbers less than 2)
        b. Iterate from 2 to the square root of the number
        c. Check if the number is divisible by any of these values
        d. Return True if the number is prime, False otherwise
    3. In the prime_length function:
        a. Calculate the length of the input string
        b. Call the is_prime function with the string length as an argument
        c. Return the result of the is_prime function
    4. Consider handling potential edge cases:
        a. Empty strings
        b. Strings with non-alphanumeric characters
    5. Return the result (True or False) indicating whether the string length is prime or not
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not string.isalnum():
        return False

    return is_prime(len(string))