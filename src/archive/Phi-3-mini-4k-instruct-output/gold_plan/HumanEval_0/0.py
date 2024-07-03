from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Iterate through the list of numbers using enumerate to access both index and value
    for i, num1 in enumerate(numbers):
        # For each number, create a nested loop to compare it with every other number in the list
        for j, num2 in enumerate(numbers):
            # Make sure to skip comparing a number with itself by checking if the indices are different
            if i != j:
                # Calculate the absolute difference between the two numbers being compared
                diff = abs(num1 - num2)
                # If the difference is less than the threshold, immediately return True
                if diff < threshold:
                    return True
    # If no close elements are found after checking all pairs, return False
    return False