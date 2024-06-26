def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Step 1: Calculate the length of the input string and store it in a variable
    length = len(string)
    
    # Step 2: Check if the length is 0 or 1
    if length <= 1:
        return False
    
    # Step 3: Create a loop that iterates from 2 to the length of the string (exclusive)
    for i in range(2, length):
        # Step 3a: Check if the length is divisible by the current number in the loop
        if length % i == 0:
            # Step 3b: If it is divisible, return False as the length is not prime
            return False
    
    # Step 4: If the loop completes without finding any divisors, return True as the length is prime
    return True