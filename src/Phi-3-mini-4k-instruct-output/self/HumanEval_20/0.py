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
        a. Check if the list has at least two elements
    
    2. Initialize:
        a. Set the closest pair as None
        b. Set the smallest distance as a large number (e.g., float('inf'))
    
    3. Sort the list to ease comparison:
        a. Use the sort method, ensuring the smallest difference is found efficiently
    
    4. Implement nested loops:
        a. Start with the first element and compare it with the rest
        b. Then move on to the next element and compare again
    
    5. Determine the closest pair and update the smallest distance:
        a. For each pair, calculate the absolute difference
        b. If the current difference is less than the smallest distance, update both the closest pair and smallest distance
    
    6. Return the closest pair (ensure order from smaller to larger)"""

    # Validate the input
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    # Initialize
    closest_pair = None
    smallest_distance = float('inf')

    # Sort the list
    numbers.sort()

    # Implement nested loops
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference
            current_distance = abs(numbers[i] - numbers[j])

            # Determine the closest pair and update the smallest distance
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                closest_pair = (numbers[i], numbers[j])

    # Return the closest pair (ensure order from smaller to larger)
    return tuple(sorted(closest_pair))