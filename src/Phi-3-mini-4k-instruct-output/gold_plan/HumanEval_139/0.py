def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.

    Action Plan:
    1. Initialize two variables:
       - One to store the factorial of the current number
       - One to store the accumulating special factorial result

    2. Create a loop that iterates from 1 to n (inclusive)

    3. Inside the loop:
       a. Update the factorial of the current number
       b. Multiply the special factorial result by the current factorial

    4. After the loop ends, return the final special factorial result

    Note: Be careful with the order of operations and make sure to update
    variables correctly in each iteration.
    """
    factorial = 1
    special_factorial_result = 1

    for i in range(1, n + 1):
        factorial *= i
        special_factorial_result *= factorial

    return special_factorial_result