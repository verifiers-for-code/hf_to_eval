from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    

    Action Plan:
    1. Split the string into a list of words using `split()`
    2. Validate each word to ensure it's a valid number ('zero' to 'nine')
    3. Convert valid words to integers and store them in a new list
    4. Sort the list of integers
    5. Create a new list of words by mapping each integer back to its corresponding string
    6. Join the list of words into a single string with spaces in between
    7. Edge case considerations:
        a. Return the sorted string if all inputs are valid
        b. Handle cases with non-numeric or out-of-range elements
        c. Return an appropriate message or error for invalid input
    
    8. Test the function with various input scenarios, including the provided examples"""
    
    # Step 1: Split the string into a list of words
    words = numbers.split()
    
    # Step 2: Validate each word to ensure it's a valid number ('zero' to 'nine')
    valid_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    valid_words = [word for word in words if word in valid_numbers]
    
    # Step 3: Convert valid words to integers and store them in a new list
    try:
        numbers_list = [int(word) for word in valid_words]
    except ValueError:
        return "Error: Invalid input. Please enter a space-delimited string of numbers from 'zero' to 'nine'."