def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    
    1. Define a helper function is_prime(n) to check if a number is prime:
       a. Check if n is less than or equal to 1, return False (not prime)
       b. Iterate from 2 to the square root of n
       c. Check if n is divisible by any of these numbers, return False (not prime)
       d. If no divisors are found, return True (prime)
    
    2. Convert the input hexadecimal string to a decimal integer:
       a. Use the int() function with base 16 to convert the string to decimal
    
    3. Initialize a counter variable to store the number of prime digits:
       a. Set the counter to 0
    
    4. Iterate through each digit in the decimal number:
       a. Convert the digit to a string
       b. Convert the string back to an integer
       c. Check if the integer is prime using the is_prime() function
       d. If the digit is prime, increment the counter
    
    5. Return the final count of prime digits:
       a. Return the value of the counter
    
    Additional implementation details:
    - Use a for loop to iterate through each digit in the decimal number
    - Use the int() function with base 16 to convert the hexadecimal string to decimal
    - Use the is_prime() function to check if a digit is prime
    - Ensure the function handles empty input strings and invalid hexadecimal digits correctly"""

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not num:
        return 0

    num_decimal = int(num, 16)
    prime_count = 0

    for digit in str(num_decimal):
        if is_prime(int(digit)):
            prime_count += 1

    return prime_count