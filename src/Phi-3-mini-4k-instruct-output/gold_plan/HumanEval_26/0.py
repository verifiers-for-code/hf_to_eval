from typing import List


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
    # Step 1: Create a dictionary to count occurrences
    count_dict = {}
    
    # Step 2: Populate the dictionary with counts
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    # Step 3: Create a new list for the result
    result = []
    
    # Step 4: Iterate through the original list and add unique elements to the result
    for number in numbers:
        if count_dict[number] == 1:
            result.append(number)
    
    # Step 5: Return the result list
    return result