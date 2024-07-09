from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    

    Action Plan:
    1. Calculate the mean of the input list of numbers:
        a. Sum up all the numbers in the list
        b. Divide the sum by the length of the list
    
    2. Calculate the absolute deviations from the mean:
        a. Create a new list to store the absolute deviations
        b. Iterate through each number in the input list:
            - Calculate the absolute difference between the number and the mean
            - Add the absolute difference to the list of absolute deviations
    
    3. Calculate the mean of the absolute deviations:
        a. Sum up all the absolute deviations in the list
        b. Divide the sum by the length of the list
    
    4. Return the final result:
        a. Return the mean of the absolute deviations as a float
    
    Note: Use appropriate mathematical operations and Python functions to perform the calculations.
    Ensure correct handling of edge cases, such as an empty input list."""
    
    # Step 1: Calculate the mean of the input list of numbers
    if len(numbers) == 0:
        return 0.0
    mean = sum(numbers) / len(numbers)
    
    # Step 2: Calculate the absolute deviations from the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Step 3: Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    # Step 4: Return the final result
    return mad