from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Action Plan:
    1. Create a data structure to count the occurrences of each number in the input list.
       Hint: Consider using a dictionary or a specialized counting tool from the collections module.
    
    2. Iterate through the input list once to populate the counting data structure.
    
    3. Create a new empty list to store the result.
    
    4. Iterate through the original input list again:
       a. For each number, check its count in the data structure.
       b. If the count is 1 (appears only once), add it to the result list.
    
    5. Return the result list containing only the unique elements, preserving the original order.
    """
    # Step 1: Count occurrences of each number using Counter from collections
    count_dict = Counter(numbers)
    
    # Step 3: Create a new empty list to store the result
    result = []
    
    # Step 4: Iterate through the original input list
    for num in numbers:
        # Step 4a: Check the count of the current number
        if count_dict[num] == 1:
            # Step 4b: If the count is 1, add it to the result list
            result.append(num)
    
    # Step 5: Return the result list containing only the unique elements, preserving the original order
    return result