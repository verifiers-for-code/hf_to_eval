from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    

    Action Plan:
    1. Initialize a flag to False, assuming no close elements are found.
    2. Iterate through the list of numbers using nested loops to compare each number with every other number.
    3. For each comparison, calculate the absolute difference between the two numbers.
    4. Check if the calculated difference is less than the given threshold.
    5. If a difference less than the threshold is found, immediately return True, indicating close elements are present.
    6. If no close elements are found after comparing all pairs of numbers, return False."""

    # Step 1: Initialize a flag to False
    has_close = False

    # Step 2: Iterate through the list of numbers using nested loops
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Step 3: Calculate the absolute difference between the two numbers
            difference = abs(numbers[i] - numbers[j])

            # Step 4: Check if the calculated difference is less than the given threshold
            if difference < threshold:
                # Step 5: If a difference less than the threshold is found, immediately return True
                has_close = True
                return has_close

    # Step 6: If no close elements are found after comparing all pairs of numbers, return False
    return has_close