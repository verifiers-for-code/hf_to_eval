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
    
    2. Initialize variables:
        - Initialize two variables to store the closest elements: `closest_smaller` and `closest_larger`
        - Set both variables to the first element of the list
    
    3. Iterate through the list:
        - For each element in the list (starting from the second element):
            a. Calculate the absolute difference between the current element and the `closest_smaller` element
            b. Calculate the absolute difference between the current element and the `closest_larger` element
            c. Compare the differences:
                - If the difference with `closest_smaller` is smaller, update `closest_smaller` with the current element
                - If the difference with `closest_larger` is smaller, update `closest_larger` with the current element
    
    4. Update the closest elements:
        - After iterating through the list, the `closest_smaller` and `closest_larger` variables will hold the two closest elements
    
    5. Return the result:
        - Return a tuple containing the `closest_smaller` and `closest_larger` elements in that order
    
    Note: Use appropriate data types and methods for calculations and comparisons.
    Be careful with the iteration and updating of variables.
    """
    # Step 1: Validate the input
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    # Step 2: Initialize variables
    closest_smaller, closest_larger = numbers[0], numbers[0]
    
    # Step 3: Iterate through the list
    for num in numbers[1:]:
        diff_smaller = abs(num - closest_smaller)
        diff_larger = abs(num - closest_larger)
        
        # Step 3a: Update closest_smaller or closest_larger
        if diff_smaller < abs(closest_smaller - closest_larger):
            closest_smaller = num
        elif diff_larger < abs(closest_smaller - closest_larger):
            closest_larger = num
    
    # Step 4: Return the result
    return (closest_smaller, closest_larger)