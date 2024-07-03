from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    # Step 1: Initialize variables to store the closest pair and their distance
    closest_pair = None
    smallest_distance = None

    # Step 2: Iterate through the list to compare each pair of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Step 3: Calculate the distance between pairs
            distance = abs(numbers[i] - numbers[j])

            # Step 4: Update the closest pair when a smaller distance is found
            if smallest_distance is None or distance < smallest_distance:
                smallest_distance = distance
                closest_pair = (numbers[i], numbers[j])

    # Step 5: Handle the case of identical numbers
    if closest_pair[0] == closest_pair[1]:
        return closest_pair

    # Step 6: Return the result in the correct order
    return tuple(sorted(closest_pair))