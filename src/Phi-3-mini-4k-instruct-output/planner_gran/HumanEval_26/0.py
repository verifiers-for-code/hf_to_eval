from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    

    1. Initialize an empty list to store the result
       - This list will hold the unique elements from the input list
    
    2. Initialize an empty set to keep track of unique elements
       - This set will store the elements that have been seen so far
    
    3. Iterate through each element in the input list:
       a. Check if the current element is not in the set of unique elements
       b. If it's not in the set:
          - Add the element to the result list
          - Add the element to the set of unique elements
    
    4. Return the result list
       - This list contains the unique elements from the input list, in the original order
    
    Additional implementation details:
    - Use a set to keep track of unique elements for efficient lookups
    - Use a list to store the result to preserve the original order
    - Iterate through the input list using a for loop or list comprehension
    - Use the 'in' operator to check if an element is in the set of unique elements
    - Use the 'add' method to add elements to the set and list
    - Ensure the function handles empty input lists correctly"""

    result = []
    seen = set()

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result