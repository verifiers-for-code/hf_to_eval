def specialFilter(nums):
    """
    This function takes an array of numbers as input and returns the number of elements in the array that are greater than 10 and both first and last digits of a number are odd (1, 3, 5, 7, 9).

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The count of numbers that meet the criteria.
    """
    count = 0
    for num in nums:
        # Extract the first and last digits of the current number
        first_digit = int(str(abs(num))[0])
        last_digit = int(str(abs(num))[-1])
        
        # Check if both digits are odd and the number is greater than 10
        if first_digit in [1, 3, 5, 7, 9] and last_digit in [1, 3, 5, 7, 9] and num > 10:
            count += 1
            
    return count