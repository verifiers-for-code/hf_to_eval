def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
    1. Handle the input n:
       - Check if n is less than or equal to 0
       - If true, return an empty list (no prime numbers to return)
    
    2. Define a helper function is_prime(num):
       - This function will check if a given number is prime
       - Implement the logic to check for primality (e.g., iterate from 2 to the square root of num, check for divisibility)
    
    3. Implement the main function count_up_to(n):
       - Initialize an empty list result to store the prime numbers
       - Iterate over numbers from 2 to n (inclusive)
       - For each number, call the is_prime function to check if it's prime
       - If the number is prime, add it to the result list
    
    4. Implement the is_prime(num) function:
       - Check if num is less than 2 (not prime)
       - Iterate from 2 to the square root of num (inclusive)
       - Check if num is divisible by any of these numbers
       - If divisible, return False (not prime)
       - If not divisible by any, return True (prime)
    
    5. Return the result list:
       - The list contains the first n prime numbers less than n
    
    Additional implementation details:
    - Use a loop or list comprehension to iterate over numbers less than n
    - Use the is_prime function to check for primality
    - Use a conditional statement to add prime numbers to the result list
    - Consider using a more efficient primality test for larger values of n"""
    
    if n <= 0:
        return []
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    result = [i for i in range(2, n) if is_prime(i)]
    
    return result