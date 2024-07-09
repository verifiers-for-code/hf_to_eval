from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    

    Action Plan:
    1. Validate the input:
        - Check if the input list has at least two elements
        - Raise a ValueError if the list has less than two elements
    
    2. Initialize the minimum difference and closest pair:
        - Set the minimum difference to a large value (e.g., positive infinity)
        - Set the closest pair to the first two elements of the list
    
    3. Iterate through the list to find the closest pair:
        - Use two nested loops to compare each pair of elements in the list
        - For each pair, calculate the absolute difference between the two elements
    
    4. Update the minimum difference and closest pair:
        - If the calculated difference is smaller than the current minimum difference:
            - Update the minimum difference with the new value
            - Update the closest pair with the current pair
    
    5. Return the closest pair:
        - Return the closest pair found in the list
    
    Note: Consider using the built-in min function with a key function to find the minimum difference and closest pair in a more concise way."""
    
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[1])
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])
    
    return closest_pair