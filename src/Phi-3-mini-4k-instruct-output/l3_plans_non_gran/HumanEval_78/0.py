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
    

    Action Plan:
    1. Define a function `hex_key` that takes a hexadecimal number as a string as input.
    2. Create a helper function `is_prime` to check if a number is prime:
        a. Define the function with a single parameter `num`.
        b. Check if `num` is less than 2, and return `False` if true.
        c. Iterate from 2 to the square root of `num` and check for divisibility.
        d. Return `True` if no divisors are found, `False` otherwise.
    3. Initialize a variable `count` to store the number of prime digits.
    4. Iterate through each character in the input hexadecimal string:
        a. Convert the character to its decimal equivalent using `ord`.
        b. Check if the decimal value is a prime number using the `is_prime` function.
        c. If the value is prime, increment the `count` variable.
    5. Return the final `count` value.
    6. Consider edge cases, such as an empty input string or invalid input."""

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for char in num:
        decimal_value = ord(char)
        if is_prime(decimal_value) and decimal_value in [2, 3, 5, 7, 11, 13]:
            count += 1
    return count