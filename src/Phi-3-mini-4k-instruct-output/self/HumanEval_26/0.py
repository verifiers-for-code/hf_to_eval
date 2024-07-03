from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    

    Action Plan:
    1. Initialize an empty list to hold unique numbers
    2. Set up a temporary dictionary (hashmap) to keep track of element occurrences.
    3. Loop over the input list with indices:
        a. Check if the current number is not in the dictionary.
        b. If it's not, add it to the unique list and the dictionary.
        c. If it is, continue to the next iteration without including it in the unique list.
    4. Return the resulting unique list"""

    unique_numbers = []
    seen_numbers = {}

    for number in numbers:
        if number not in seen_numbers:
            unique_numbers.append(number)
            seen_numbers[number] = True

    return unique_numbers