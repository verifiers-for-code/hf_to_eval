from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    

    Action Plan:
    1. Split the input string into a list of strings using the space character as the separator.
    2. Create a dictionary to map the strings to their corresponding integer values.
    3. Iterate through the list of strings:
        a. Check if the current string is a valid number (i.e., exists in the dictionary).
        b. If it's a valid number, convert it to an integer and add it to a separate list of numbers.
    4. Sort the list of numbers in ascending order.
    5. Join the sorted list of numbers back into a string using the space character as the separator.
    6. Return the final sorted string.
    
    Note: Use appropriate string and list methods for parsing, validation, and sorting.
    Be careful to handle invalid input strings correctly."""
    
    # Step 1: Split the input string into a list of strings using the space character as the separator.
    number_list = numbers.split()
    
    # Step 2: Create a dictionary to map the strings to their corresponding integer values.
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # Step 3: Iterate through the list of strings:
    # a. Check if the current string is a valid number (i.e., exists in the dictionary).
    # b. If it's a valid number, convert it to an integer and add it to a separate list of numbers.
    numbers_list = []
    for number in number_list:
        if number in number_dict:
            numbers_list.append(number_dict[number])
        else:
            raise ValueError(f"Invalid input: {number} is not a valid number.")
    
    # Step 4: Sort the list of numbers in ascending order.
    numbers_list.sort()
    
    # Step 5: Join the sorted list of numbers back into a string using the space character as the separator.
    sorted_numbers = ' '.join(str(num) for num in numbers_list)
    
    # Step 6: Return the final sorted string.
    return sorted_numbers