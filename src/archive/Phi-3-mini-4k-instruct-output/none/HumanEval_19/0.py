from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map the words to their corresponding numbers
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
    
    # Split the input string into a list of words
    words = numbers.split()
    
    # Convert the words to numbers using the dictionary
    numbers_list = [number_dict[word] for word in words]
    
    # Sort the list of numbers
    numbers_list.sort()
    
    # Convert the sorted numbers back to words
    sorted_words = [list(number_dict.keys())[list(number_dict.values()).index(num)] for num in numbers_list]
    
    # Join the sorted words into a string
    sorted_numbers = ' '.join(sorted_words)
    
    return sorted_numbers