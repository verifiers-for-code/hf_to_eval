def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b using the Euclidean algorithm.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    
    Example:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Step 1: Define the function
    def gcd_recursive(a: int, b: int) -> int:
        # Step 2: Implement the Euclidean algorithm
        if b == 0:
            # Step 3: Handle the base case
            return a
        else:
            # Step 4: Perform the recursive step
            return gcd_recursive(b, a % b)
    
    # Step 5: Return the final result
    return gcd_recursive(a, b)