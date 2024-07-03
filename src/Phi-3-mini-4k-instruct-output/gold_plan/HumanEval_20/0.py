from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)

    Action Plan:
    1. Initialize variables to store the closest pair and their distance:
       - Create variables for the closest pair (initially None) and the smallest distance (initially None)

    2. Iterate through the list to compare each pair of numbers:
       - Use nested loops to compare each number with every other number in the list
       - Ensure you don't compare a number with itself

    3. Calculate the distance between pairs:
       - Use the absolute difference between two numbers as the distance

    4. Update the closest pair when a smaller distance is found:
       - If it's the first pair or if the new distance is smaller than the current smallest distance:
         a. Update the smallest distance
         b. Update the closest pair

    5. Handle the case of identical numbers:
       - If two numbers are identical, they should be considered as the closest pair

    6. Return the result in the correct order:
       - Ensure the smaller number is first in the returned tuple
       - Use tuple(sorted([...])) to achieve this
    """
    closest_pair = None
    smallest_distance = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if smallest_distance is None or distance < smallest_distance:
                smallest_distance = distance
                closest_pair = (numbers[i], numbers[j])

    return tuple(sorted(closest_pair))