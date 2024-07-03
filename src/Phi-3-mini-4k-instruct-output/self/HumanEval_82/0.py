def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    

    Action Plan:
    1. Prime number definition:
        - Define a prime number as a number greater than 1, that has no divisors other than 1 and itself
    
    2. Create a function to check if a number is prime:
        - Handle edge cases: return False for numbers less than or equal to 1
        - Use a loop to check divisibility by all numbers from 2 to the square root of the input
    
    3. Implement the function in the main `prime_length()` function:
        - Calculate the length of the input string
        - Use the prime-checking function to determine if the length is prime
    
    4. Handle edge cases in `prime_length()`:
        - Return False for empty strings or non-string inputs
        - Ensure non-string inputs do not throw errors
    
    5. Optimize the prime-checking function for large numbers, if needed
    
    6. Test the function with provided examples and additional edge cases (e.g., very long strings, strings with special characters)"""
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if not isinstance(string, str):
        return False
    
    return is_prime(len(string))