def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    

    Action Plan:
    1. Set a counter to 0 for the number of occurrences of 7
    2. Start a loop from 1 up to, but not including, n (use n-1 to handle the exclusivity of the range)
        a. Convert each number to a string for easy digit checking
    3. Within the loop, use modulo and division operations to check if the number is divisible by 11 or 13
        a. Perform divisibility checks (e.g., (number % 11 == 0) or (number % 13 == 0))
    4. If the number is divisible by either 11 or 13, convert the string to a list of individual characters (digits)
    5. Filter the list of characters to find digits that are '7'
        a. If there are '7's in the list, add to the counter
    6. Continue looping until the end
    7. Return the final count"""
    count = 0
    for number in range(1, n):
        if number % 11 == 0 or number % 13 == 0:
            digits = list(str(number))
            count += digits.count('7')
    return count