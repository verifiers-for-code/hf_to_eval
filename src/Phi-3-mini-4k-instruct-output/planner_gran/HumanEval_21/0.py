from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    Parameters:
    numbers (List[float]): A list of numbers to be rescaled.
    
    Returns:
    List[float]: A list of rescaled numbers.
    
    Raises:
    ValueError: If the input is not a list or has less than two elements.
    
    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    
    # Validate the input
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")
    
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Calculate the scaling factor
    scaling_factor = (max_val - min_val) / max_val
    
    # Apply the linear transformation to each number
    rescaled_numbers = [(num - min_val) / scaling_factor for num in numbers]
    
    # Return the transformed list
    return rescaled_numbers