def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    

    Action Plan:
    1. Initialize a variable `count` to 0 to store the count of digit 7.
    2. Iterate through numbers from 0 to `n-1` (inclusive).
    3. For each number, check if it is divisible by 11 or 13 using the modulo operator (%).
    4. If the number is divisible, convert it to a string to access its digits.
    5. Iterate through each digit in the string representation of the number:
        a. Check if the current digit is '7'.
        b. If it is, increment the `count` variable.
    6. After processing all numbers, return the final value of `count`.
    7. Consider edge cases, such as an empty input or invalid input types.
    
    Note: Use appropriate data types and operations to implement the solution.
    Be mindful of the problem constraints and requirements."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            for digit in str(i):
                if digit == '7':
                    count += 1
    return count