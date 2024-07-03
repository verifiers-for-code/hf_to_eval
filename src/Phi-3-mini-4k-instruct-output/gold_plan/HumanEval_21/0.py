from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
    Action Plan:
    1. Find the minimum value in the input list 'numbers'.
    2. Find the maximum value in the input list 'numbers'.
    3. Calculate the range by subtracting the minimum from the maximum.
    4. Create a new list by applying the following transformation to each number 'x' in 'numbers':
       a. Subtract the minimum value from 'x'.
       b. Divide the result by the range calculated in step 3.
    5. Return the new list containing the transformed values.
    
    Note: Ensure to handle potential division by zero if all numbers in the list are the same.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    if min_val == max_val:
        return [0.0] * len(numbers)
    
    range_val = max_val - min_val
    
    return [(x - min_val) / range_val for x in numbers]