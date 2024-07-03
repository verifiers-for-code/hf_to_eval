def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1

    Action Plan:
    1. Initialize a variable to store the result, starting with the base case for 2^0.
    2. Create a loop that iterates 'n' times to calculate 2^n.
    3. In each iteration:
       a. Multiply the current result by 2.
       b. Apply modulo p to the multiplication result to keep the number small.
    4. After the loop completes, return the final result.

    Note: This approach avoids calculating large numbers directly and uses the
    properties of modular arithmetic to compute the result efficiently.
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result