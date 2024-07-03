from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
    Action Plan:
    1. Find the minimum and maximum values in the list:
        a. Initialize min_val and max_val with the first element of the list
        b. Iterate through the rest of the list, updating min_val and max_val
    
    2. Calculate the range of the values:
        a. The range is the difference between the max_val and min_val
    
    3. Apply the linear transformation formula to scale each number:
        a. Initialize an empty list for the results
        b. For each number in the original list, calculate its scaled value using the formula:
            scaled_value = (number - min_val) / range
    
    4. Handle edge cases:
        a. Check if the range is zero (which means all numbers in the list are the same) and handle this case properly.
    
    5. Return the list of scaled values
    """
    # Step 1: Find the minimum and maximum values in the list
    min_val = numbers[0]
    max_val = numbers[0]
    for number in numbers[1:]:
        if number < min_val:
            min_val = number
        elif number > max_val:
            max_val = number
    
    # Step 2: Calculate the range of the values
    range_val = max_val - min_val
    
    # Step 3: Apply the linear transformation formula to scale each number
    scaled_values = []
    if range_val == 0:
        # Handle edge case where all numbers are the same
        return [0.0] * len(numbers)
    
    for number in numbers:
        scaled_value = (number - min_val) / range_val
        scaled_values.append(scaled_value)
    
    return scaled_values