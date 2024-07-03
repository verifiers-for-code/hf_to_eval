def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    

    Action Plan:
    1. Define a function `fizz_buzz` that takes an integer `n` as input.
    2. Create a helper function `is_divisible` to check if a number is divisible by 11 or 13.
        - This function should take an integer `num` as input and return `True` if `num` is divisible by 11 or 13, and `False` otherwise.
    3. Initialize a variable `count` to store the count of occurrences of the digit 7.
    4. Iterate through the range of numbers from 1 to `n-1` (inclusive).
        - For each number in the range, check if it is divisible by 11 or 13 using the `is_divisible` function.
        - If the number is divisible, convert it to a string and count the occurrences of the digit 7 using the `count` method.
        - Add the count to the `count` variable.
    5. Return the final `count` value.
    
    Note: Be careful when iterating through the range of numbers and converting them to strings for counting the occurrences of the digit 7."""
    
    def is_divisible(num: int) -> bool:
        return num % 11 == 0 or num % 13 == 0
    
    count = 0
    for i in range(1, n):
        if is_divisible(i):
            count += str(i).count('7')
    
    return count