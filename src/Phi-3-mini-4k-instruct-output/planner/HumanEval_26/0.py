from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    

    Action Plan:
    1. Understand the problem: Remove duplicates from a list of integers while preserving the original order.
    2. Create a data structure (e.g., a set) to keep track of elements that have already been seen.
    3. Initialize an empty list to store the unique elements.
    4. Iterate through the input list of numbers:
        a. For each number, check if it's not in the set of seen elements.
        b. If the number is not seen, add it to the set of seen elements and the list of unique elements.
    5. Return the list of unique elements.
    
    Note: Use a set to efficiently check for duplicates and preserve the original order of elements.
    Be careful to update the set and list correctly during iteration."""

    seen = set()
    unique_numbers = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique_numbers.append(number)

    return unique_numbers