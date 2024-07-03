from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
    Action Plan:
    1. Create a data structure to count the occurrences of each number in the input list.
       Hint: Consider using a dictionary or a specialized counting tool from the collections module.
    
    2. Iterate through the input list once to populate the counting data structure.
    
    3. Create a new empty list to store the result.
    
    4. Iterate through the original input list again:
       a. For each number, check its count in the data structure.
       b. If the count is 1 (appears only once), add it to the result list.
    
    5. Return the result list containing only the unique elements, preserving the original order.
    
    Note: Try to implement this solution in a single pass through the list if possible,
    but prioritize correctness over optimization initially.
    """
    # Step 1: Count occurrences using Counter from collections
    count_dict = Counter(numbers)
    
    # Step 2: Populate the count_dict in a single pass
    unique_numbers = []
    for number in numbers:
        if count_dict[number] == 1:
            unique_numbers.append(number)
    
    return unique_numbers