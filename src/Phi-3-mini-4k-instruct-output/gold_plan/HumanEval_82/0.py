def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False

    Action Plan:
    1. Calculate the length of the input string and store it in a variable.
    2. Check if the length is 0 or 1. If so, return False as these are not prime numbers.
    3. Create a loop that iterates from 2 to the length of the string (exclusive):
       a. Check if the length is divisible by the current number in the loop.
       b. If it is divisible, return False as the length is not prime.
    4. If the loop completes without finding any divisors, return True as the length is prime.
    """
    length = len(string)
    if length < 2:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True