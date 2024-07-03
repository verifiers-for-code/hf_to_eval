from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    

    Action Plan:
    1. Find the minimum and maximum values in the input list of numbers.
    2. Define the linear transformation formula to rescale the numbers:
       a. Subtract the minimum value from each number to shift the range to start from 0.
       b. Divide the result by the difference between the maximum and minimum values to scale the range to [0, 1].
    3. Apply this transformation to each number in the input list:
       a. For each number, calculate the transformed value using the defined formula.
       b. Store the transformed values in a new list.
    4. Return the new list containing the rescaled numbers."""

    # Step 1: Find the minimum and maximum values in the input list of numbers
    min_val = min(numbers)
    max_val = max(numbers)

    # Step 2: Define the linear transformation formula to rescale the numbers
    # a. Subtract the minimum value from each number to shift the range to start from 0
    # b. Divide the result by the difference between the maximum and minimum values to scale the range to [0, 1]
    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    # Step 3: Apply this transformation to each number in the input list
    # a. For each number, calculate the transformed value using the defined formula
    # b. Store the transformed values in a new list

    # Step 4: Return the new list containing the rescaled numbers
    return rescaled_numbers