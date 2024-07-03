from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Action Plan:
    1. Calculate the mean of the input numbers:
       - Use a loop or the built-in sum function to calculate the sum of all numbers in the list
       - Divide the sum by the length of the list to get the mean
    
    2. Calculate the absolute differences between each number and the mean:
       - Use a list comprehension or a loop to iterate over the input numbers
       - For each number, calculate the absolute difference between the number and the mean
       - Store these absolute differences in a new list
    
    3. Calculate the mean of the absolute differences:
       - Use the sum function to calculate the sum of the absolute differences
       - Divide the sum by the length of the list to get the mean absolute difference
    
    4. Return the mean absolute difference as the result:
       - The function should return a float value representing the mean absolute deviation
    
    Additional implementation details:
    - Use the appropriate data types and variables to store the input numbers, mean, and absolute differences
    - Ensure that the function handles empty input lists correctly
    - Consider using the built-in abs function to calculate the absolute difference between each number and the mean
    - Use the sum function to calculate the sum of the absolute differences and the mean of the input numbers
    """
    if not numbers:
        return 0.0
    
    mean = sum(numbers) / len(numbers)
    absolute_differences = [abs(x - mean) for x in numbers]
    mean_absolute_deviation = sum(absolute_differences) / len(numbers)
    
    return mean_absolute_deviation