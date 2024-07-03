from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    Action Plan:
    1. Initialize an empty list to store the rolling maximum elements:
       - This list will hold the maximum elements found until each moment in the sequence
    
    2. Initialize a variable to store the maximum element seen so far:
       - Set this variable to the first element of the input list (or a default value if the list is empty)
    
    3. Iterate through the input list, starting from the second element:
       - For each element in the list:
         a. Check if the current element is greater than the maximum element seen so far
         b. If it is, update the maximum element seen so far to the current element
         c. Append the maximum element seen so far to the result list
    
    4. After iterating through the entire list, return the result list:
       - This list now contains the rolling maximum elements found until each moment in the sequence
    
    Additional implementation details:
    - Use a loop to iterate through the input list
    - Use a conditional statement to check if the current element is greater than the maximum element seen so far
    - Use the append method to add the maximum element to the result list
    - Ensure that the function handles empty input lists correctly
    - Consider adding type hints and a docstring to the function for clarity and documentation
    """
    if not numbers:
        return []
    
    result = [numbers[0]]
    max_seen = numbers[0]
    
    for num in numbers[1:]:
        if num > max_seen:
            max_seen = num
        result.append(max_seen)
    
    return result