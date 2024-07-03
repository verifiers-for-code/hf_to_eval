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
    1. Define the function `special_factorial` with an integer parameter `n`.
    2. Handle the base case:
        - If `n` is 1, return 1 (since 1! = 1)
    3. Implement the recursive case:
        - If `n` is greater than 1, calculate the special factorial by:
            a. Calculating the factorial of `n` (n!)
            b. Calculating the factorial of `n-1` (n-1!)
            c. Calculating the factorial of `n-2` (n-2!)
            d. Multiply these three factorials together
    4. Return the calculated special factorial
    5. Consider adding error handling for invalid input (e.g., negative numbers)"""

    # Base case
    if n == 1:
        return 1

    # Recursive case
    else:
        # Calculate factorial of n
        n_factorial = special_factorial(n-1)

        # Calculate factorial of n-1
        n_minus_1_factorial = special_factorial(n-2)

        # Calculate factorial of n-2
        n_minus_2_factorial = special_factorial(n-3)

        # Multiply the three factorials together
        special_factorial_value = n_factorial * n_minus_1_factorial * n_minus_2_factorial

        return special_factorial_value