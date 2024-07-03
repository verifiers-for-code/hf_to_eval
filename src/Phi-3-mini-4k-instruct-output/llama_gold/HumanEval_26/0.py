from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    

    Action Plan:
    1. Create a data structure to count the occurrences of each number in the input list.
    2. Iterate through the input list to count the occurrences of each number.
    3. Initialize an empty result list to store the unique numbers.
    4. Iterate through the input list again:
       a. Check the count of the current number.
       b. If the count is 1, add the number to the result list.
    5. Return the result list containing only the numbers that occur once in the input list, in their original order."""
    
    # Step 1: Create a dictionary to count occurrences
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Step 3: Initialize an empty result list
    result = []
    
    # Step 4: Iterate through the input list again
    for num in numbers:
        # Step 4a: Check the count of the current number
        if count_dict[num] == 1:
            # Step 4b: If the count is 1, add the number to the result list
            result.append(num)
    
    # Step 5: Return the result list
    return result