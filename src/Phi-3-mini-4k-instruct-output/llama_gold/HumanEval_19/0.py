from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    

    Action Plan:
    1. Create a dictionary (value_map) to map number words ('zero' to 'nine') to their corresponding integer values (0 to 9).
    2. Split the input string into a list of individual number words using the space character as the delimiter.
    3. Filter the list to remove any invalid number words that are not present in the value_map.
    4. Sort the filtered list of number words based on their corresponding integer values in the value_map.
    5. Join the sorted list of number words back into a single string, separated by spaces.
    6. Return the resulting sorted string."""

    # Step 1: Create a dictionary to map number words to their corresponding integer values
    value_map = {
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

    # Step 2: Split the input string into a list of individual number words
    number_words = numbers.split()

    # Step 3: Filter the list to remove any invalid number words
    valid_number_words = [word for word in number_words if word in value_map]

    # Step 4: Sort the filtered list of number words based on their corresponding integer values
    sorted_number_words = sorted(valid_number_words, key=lambda word: value_map[word])

    # Step 5: Join the sorted list of number words back into a single string, separated by spaces
    sorted_numbers = ' '.join(sorted_number_words)

    # Step 6: Return the resulting sorted string
    return sorted_numbers