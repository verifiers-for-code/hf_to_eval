from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    # Initialize variables to store the closest pair and their distance
    closest_pair = None
    smallest_distance = None

    # Iterate through the list to compare each pair of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the distance between pairs
            distance = abs(numbers[i] - numbers[j])

            # Update the closest pair when a smaller distance is found
            if smallest_distance is None or distance < smallest_distance:
                smallest_distance = distance
                closest_pair = (numbers[i], numbers[j])

    # Return the result in the correct order
    return tuple(sorted(closest_pair))