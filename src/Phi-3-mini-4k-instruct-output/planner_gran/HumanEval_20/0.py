from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    

    1. Handle the input list of numbers:
       - Ensure the input is a list of at least two numbers
       - Convert the list to a sorted list in ascending order
    
    2. Initialize variables to store the closest pair of numbers:
       - Initialize two variables, closest_pair and min_diff, to store the closest pair of numbers and the minimum difference between them
    
    3. Iterate through the sorted list of numbers:
       - Use nested loops to compare each pair of adjacent numbers
       - For each pair, calculate the absolute difference between the two numbers
       - If the difference is less than min_diff, update min_diff and closest_pair with the current pair
    
    4. Return the closest pair of numbers in order:
       - After iterating through the entire list, return the closest_pair in order (smaller number, larger number)
    
    Additional implementation details:
    - Use a suitable data structure to store the sorted list of numbers
    - Implement the nested loops efficiently to avoid unnecessary iterations
    - Use the appropriate method to calculate the absolute difference between two numbers
    - Ensure the function handles edge cases, such as an empty input list or a list with only one element"""

    # Step 1: Handle the input list of numbers
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    numbers.sort()

    # Step 2: Initialize variables to store the closest pair of numbers
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])

    # Step 3: Iterate through the sorted list of numbers
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[j] - numbers[i])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    # Step 4: Return the closest pair of numbers in order
    return closest_pair