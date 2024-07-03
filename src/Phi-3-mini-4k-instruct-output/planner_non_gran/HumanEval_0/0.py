from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    

    Action Plan:
    1. Understand the problem:
        - The function takes a list of numbers and a threshold as input
        - The goal is to check if any two numbers in the list are closer to each other than the given threshold
    
    2. Initialize a variable to store the result (default to False)
    
    3. Iterate through the list of numbers:
        - For each number, iterate through the rest of the list (excluding the current number)
        - Calculate the absolute difference between the current number and the other number
        - Check if the difference is less than or equal to the threshold
        - If true, set the result to True and break the loop
    
    4. Return the result:
        - If the result is True, it means there are two numbers closer to each other than the threshold
        - If the result is False, it means no two numbers are closer to each other than the threshold
    
    Note: Use appropriate data structures and methods for iteration and comparison.
    Be careful with the indexing and slicing of the list."""
    
    result = False
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                result = True
                break
    return result