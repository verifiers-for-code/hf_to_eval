from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad