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
    1. Calculate the mean of the input numbers by summing them up and dividing by the count of numbers.
    2. Initialize a variable to store the sum of absolute differences.
    3. Iterate through each number in the input list:
       a. Calculate the absolute difference between the current number and the mean.
       b. Add this difference to the sum of absolute differences.
    4. Calculate the Mean Absolute Deviation (MAD) by dividing the sum of absolute differences by the count of numbers.
    5. Return the calculated MAD value."""

    # Step 1: Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Step 2: Initialize a variable to store the sum of absolute differences
    sum_of_absolute_differences = 0

    # Step 3: Iterate through each number in the input list
    for number in numbers:
        # Step 3a: Calculate the absolute difference between the current number and the mean
        absolute_difference = abs(number - mean)

        # Step 3b: Add this difference to the sum of absolute differences
        sum_of_absolute_differences += absolute_difference

    # Step 4: Calculate the Mean Absolute Deviation (MAD)
    mad = sum_of_absolute_differences / len(numbers)

    # Step 5: Return the calculated MAD value
    return mad