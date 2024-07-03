def sum_of_digits(num):
    """
    Calculate the sum of digits of a number.
    
    Args:
    num (int): The input number.
    
    Returns:
    int: The sum of digits of the input number.
    """
    # Convert the number to a string to access individual digits
    num_str = str(num)
    
    # Iterate through each digit, convert it back to an integer, and add it to the sum
    sum_digits = sum(int(digit) for digit in num_str)
    
    return sum_digits

def count_nums(arr):
    """
    Count the number of elements in an array of integers that have a sum of digits > 0.
    
    Args:
    arr (list): The input array of integers.
    
    Returns:
    int: The count of elements with a sum of digits > 0.
    
    Examples:
    >>> count_nums([])
    0
    >>> count_nums([-1, 11, -11])
    1
    >>> count_nums([1, 1, 2])
    3
    """
    # Initialize a counter variable to store the count
    count = 0
    
    # Iterate through each number in the input array
    for num in arr:
        # Check if the number is negative
        if num < 0:
            # Calculate the sum of its signed digits using the `sum_of_digits` function
            sum_signed_digits = sum_of_digits(abs(num))
            
            # If the sum is greater than 0, increment the counter
            if sum_signed_digits > 0:
                count += 1
        else:
            # If the number is non-negative, calculate the sum of its digits
            sum_digits = sum_of_digits(num)
            
            # If the sum is greater than 0, increment the counter
            if sum_digits > 0:
                count += 1
                
    # Return the final count
    return count