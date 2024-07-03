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
        - Use the sum function to calculate the total sum of the numbers
        - Divide the sum by the length of the list to get the mean
    
    2. Calculate the absolute differences between each element and the mean:
        - Use a list comprehension to iterate over each number in the list
        - Calculate the absolute difference between the number and the mean using the abs function
    
    3. Calculate the mean of the absolute differences:
        - Use the sum function to calculate the total sum of the absolute differences
        - Divide the sum by the length of the list to get the mean absolute deviation
    
    4. Return the mean absolute deviation as a float value
    
    Note: Use appropriate mathematical operations and functions to perform the calculations.
    Be careful with the order of operations and the use of parentheses."""
    
    # Step 1: Calculate the mean of the input list of numbers
    mean = sum(numbers) / len(numbers)
    
    # Step 2: Calculate the absolute differences between each element and the mean
    absolute_differences = [abs(x - mean) for x in numbers]
    
    # Step 3: Calculate the mean of the absolute differences
    mean_absolute_deviation = sum(absolute_differences) / len(numbers)
    
    # Step 4: Return the mean absolute deviation as a float value
    return mean_absolute_deviation