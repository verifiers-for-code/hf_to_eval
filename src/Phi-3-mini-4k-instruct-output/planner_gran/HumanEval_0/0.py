from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    

    1. Define the function with the required parameters:
       - `numbers`: a list of float numbers
       - `threshold`: a float number representing the minimum distance between two numbers
    
    2. Initialize a variable to store the result (default: False)
    
    3. Iterate through the list of numbers using a nested loop:
       a. For each number in the list, iterate through the rest of the list (from the next element to the end)
       b. Calculate the absolute difference between the current number and the other number
    
    4. Check if the absolute difference is less than the threshold:
       - If true, set the result variable to True and break the loop (exit early)
    
    5. After the loop, return the result:
       - If the result variable is True, it means there are two numbers closer than the threshold
       - If the result variable is False, it means no two numbers are closer than the threshold
    
    Additional implementation details:
    - Use a nested loop to compare each number with the rest of the list
    - Use the absolute difference (abs() function) to compare the numbers
    - Use a conditional statement (if) to check if the difference is less than the threshold
    - Use a break statement to exit the loop early if a close pair is found
    - Return a boolean value indicating whether any close pair was found"""

    result = False
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                result = True
                break
    return result