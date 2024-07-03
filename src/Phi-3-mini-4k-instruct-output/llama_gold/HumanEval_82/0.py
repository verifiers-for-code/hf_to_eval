def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    

    Action Plan:
    1. Calculate the length of the input string.
    2. Check if the length is 0 or 1, and return False if true (as 0 and 1 are not prime numbers).
    3. Define a prime number as a natural number greater than 1 that has no positive divisors other than 1 and itself.
    4. Implement a primality test:
       a. Iterate from 2 to the length - 1.
       b. Check if the length is divisible by the current number.
       c. If it is, return False (as the length is not prime).
    5. If the primality test passes (no divisors found), return True (the length is prime)."""
    
    # Step 1: Calculate the length of the input string
    length = len(string)
    
    # Step 2: Check if the length is 0 or 1
    if length <= 1:
        return False
    
    # Step 3: Implement a primality test
    for i in range(2, length):
        # Step 4a: Check if the length is divisible by the current number
        if length % i == 0:
            # Step 4c: If it is, return False
            return False
    
    # Step 5: If the primality test passes, return True
    return True