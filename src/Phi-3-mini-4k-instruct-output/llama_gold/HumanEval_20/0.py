from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    

    Action Plan:
    1. Initialize variables to store the closest pair of numbers and their distance.
    2. Iterate through the list of numbers:
       a. For each number, iterate through the list again to compare it with every other number.
       b. Calculate the absolute difference (distance) between the two numbers.
       c. If this is the first comparison or the distance is smaller than the current minimum:
          - Update the closest pair with the current two numbers (in sorted order).
          - Update the minimum distance.
    3. After comparing all pairs of numbers, return the closest pair."""

    # Step 1: Initialize variables to store the closest pair of numbers and their distance
    closest_pair = (float('inf'), float('inf'))
    min_distance = float('inf')

    # Step 2: Iterate through the list of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Step 2a: Calculate the absolute difference (distance) between the two numbers
            distance = abs(numbers[i] - numbers[j])

            # Step 2c: If this is the first comparison or the distance is smaller than the current minimum
            if distance < min_distance:
                # Update the closest pair with the current two numbers (in sorted order)
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
                # Update the minimum distance
                min_distance = distance

    # Step 3: After comparing all pairs of numbers, return the closest pair
    return closest_pair