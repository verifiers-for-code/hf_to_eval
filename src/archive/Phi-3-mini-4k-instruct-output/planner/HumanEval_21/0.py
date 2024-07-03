from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]

    Action Plan:
    1. Understand the problem: The goal is to rescale a list of numbers so that the smallest number becomes 0 and the largest becomes 1.
    2. Find the minimum and maximum values in the input list:
        - Use the built-in `min()` and `max()` functions to find the smallest and largest numbers in the list.
    3. Apply the linear transformation to each element:
        - Iterate through each number in the list.
        - For each number, subtract the minimum value and divide by the range (maximum - minimum).
        - This will rescale the number to a value between 0 and 1.
    4. Return the transformed list:
        - Store the transformed numbers in a new list.
        - Return the new list as the result.

    Note: Be careful with the order of operations to avoid division by zero.
    Use the `min()` and `max()` functions to find the smallest and largest numbers in the list.
    Apply the linear transformation to each element using the formula: (number - min) / (max - min).
    """
    min_val = min(numbers)
    max_val = max(numbers)

    if max_val - min_val == 0:
        raise ValueError("Cannot rescale list, as all elements are the same.")

    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled_numbers