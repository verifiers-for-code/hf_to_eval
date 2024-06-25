from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Apply the linear transformation
    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]
    
    return rescaled_numbers