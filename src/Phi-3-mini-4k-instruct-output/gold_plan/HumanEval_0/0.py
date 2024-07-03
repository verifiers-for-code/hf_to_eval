from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True

    Action Plan:
    1. Iterate through the list of numbers using enumerate to access both index and value.
    2. For each number, create a nested loop to compare it with every other number in the list.
    3. Make sure to skip comparing a number with itself by checking if the indices are different.
    4. Calculate the absolute difference between the two numbers being compared.
    5. If the difference is less than the threshold, immediately return True.
    6. If no close elements are found after checking all pairs, return False.
    """
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i != j and abs(num1 - num2) < threshold:
                return True
    return False