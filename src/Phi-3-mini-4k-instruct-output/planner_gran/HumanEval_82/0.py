def prime_length(string):
    """
    Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
    1. Define a helper function is_prime(n) to check if a number is prime:
       a. Initialize a variable to store the result (default to True)
       b. Check if n is less than 2 (not prime)
       c. Iterate from 2 to the square root of n (inclusive)
       d. For each iteration, check if n is divisible by the current number
       e. If n is divisible, set the result to False and break the loop
       f. Return the result (True if prime, False otherwise)
    
    2. Define the prime_length(string) function:
       a. Take a string as input
       b. Get the length of the input string
    
    3. Check if the length of the input string is prime:
       a. Call the is_prime helper function with the length as an argument
       b. Store the result in a variable
    
    4. Return the result:
       a. If the result is True, return True (length is prime)
       b. If the result is False, return False (length is not prime)
    
    Additional implementation details:
    - Use the len() function to get the length of the input string
    - Use a for loop or a while loop to iterate from 2 to the square root of n in the is_prime function
    - Use the modulo operator (%) to check for divisibility in the is_prime function
    - Ensure that the function handles empty input strings correctly"""
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if len(string) == 0:
        return False
    return is_prime(len(string))