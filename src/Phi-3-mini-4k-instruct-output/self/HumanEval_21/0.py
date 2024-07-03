from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
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
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    if min_val == max_val:
        return [0.0] * len(numbers)
    
    range_val = max_val - min_val
    scaled_values = [(num - min_val) / range_val for num in numbers]
    
    return scaled_values