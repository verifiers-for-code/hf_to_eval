def factorial(n):
    """Calculate the factorial of a single number using recursion.
    
    Args:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def special_factorial(n):
    """Calculate the special factorial of a given number.
    
    Args:
    n (int): The number to calculate the special factorial of.
    
    Returns:
    int: The special factorial of the input number.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    
    result = 1
    for i in range(n, 0, -1):
        result *= factorial(i)
    
    return result