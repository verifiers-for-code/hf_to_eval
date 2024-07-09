from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    
    Parameters:
    - numbers (List[float]): A list of float numbers.
    - threshold (float): A float representing the maximum allowed difference between two numbers.
    
    Returns:
    - bool: True if there are two numbers within the threshold distance, False otherwise.
    
    Examples:
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Initialize the result variable to False
    has_close_pair = False
    
    # Iterate through the list using a nested loop
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between the current pair of numbers
            difference = abs(numbers[i] - numbers[j])
            
            # Check if the difference is less than the given threshold
            if difference < threshold:
                # Set the result to True and break out of the inner loop
                has_close_pair = True
                break
    
    # Return the result
    return has_close_pair