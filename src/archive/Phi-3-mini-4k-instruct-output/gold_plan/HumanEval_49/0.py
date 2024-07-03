def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulo.

    Returns:
    int: The result of 2^n modulo p.

    Action Plan:
    1. Initialize a variable to store the result, starting with the base case for 2^0.
    2. Create a loop that iterates 'n' times to calculate 2^n.
    3. In each iteration:
       a. Multiply the current result by 2.
       b. Apply modulo p to the multiplication result to keep the number small.
    4. After the loop completes, return the final result.
    """
    result = 1  # Step 1: Initialize result with base case (2^0 = 1)
    for _ in range(n):  # Step 2: Iterate 'n' times
        result = (result * 2) % p  # Step 3a: Multiply by 2 and apply modulo p
    return result  # Step 4: Return the final result