def is_prime(n):
    """Check if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    """Calculate the sum of digits of a number.
    
    Args:
    n (int): The number to calculate the sum of digits for.
    
    Returns:
    int: The sum of digits of n.
    """
    return sum(int(digit) for digit in str(n))

def skjkasdkd(lst):
    """Find the largest prime value in a list and return the sum of its digits.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The sum of digits of the largest prime value in lst.
    
    Raises:
    ValueError: If the input list is empty or contains non-integer values.
    """
    if not lst:
        raise ValueError("Input list is empty.")
    
    max_prime = 0
    max_prime_index = -1
    
    for index, num in enumerate(lst):
        if not isinstance(num, int):
            raise ValueError("Input list contains non-integer values.")
        
        if is_prime(num) and num > max_prime:
            max_prime = num
            max_prime_index = index
    
    if max_prime == 0:
        raise ValueError("No prime numbers found in the list.")
    
    return sum_of_digits(max_prime)