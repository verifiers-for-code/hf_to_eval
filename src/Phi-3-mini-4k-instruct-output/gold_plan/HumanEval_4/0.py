from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Step 1: Calculate the mean of the input list 'numbers'
    mean = sum(numbers) / len(numbers)

    # Step 2: Compute the absolute differences
    absolute_differences = [abs(x - mean) for x in numbers]

    # Step 3: Calculate the average of the absolute differences
    mad = sum(absolute_differences) / len(absolute_differences)

    # Step 4: Return the final result (Mean Absolute Deviation)
    return mad