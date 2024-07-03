def special_factorial(n):
    """
    The Brazilian factorial is defined as:
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
    5. Consider adding error handling for invalid input (e.g., negative numbers)
    """
    if n < 1:
        raise ValueError("Input must be a positive integer")
    elif n == 1:
        return 1
    else:
        return n * special_factorial(n-1) * special_factorial(n-2)