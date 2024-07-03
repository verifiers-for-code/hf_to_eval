from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Action Plan:
    1. Split the input string into a list of words using the space character as a delimiter.
    2. Create an empty list to store the numbers.
    3. Iterate through each word in the list:
        a. Check if the word is a valid number ('zero' to 'nine').
        b. If valid, convert the word to an integer and add it to the list of numbers.
    4. Sort the list of numbers in ascending order.
    5. Create an empty list to store the sorted numbers as strings.
    6. Iterate through each number in the sorted list:
        a. Convert the number to a string.
        b. Add the string to the list of sorted numbers.
    7. Join the list of sorted numbers with spaces to create the final string.
    8. Return the sorted string.
    
    Note: Use appropriate string and list methods for parsing, sorting, and joining.
    Be careful when converting between strings and integers.
    """
    # Step 1: Split the input string into a list of words
    words = numbers.split(' ')
    
    # Step 2: Create an empty list to store the numbers
    numbers_list = []
    
    # Step 3: Iterate through each word in the list
    for word in words:
        # Check if the word is a valid number
        if word in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            # Convert the word to an integer and add it to the list of numbers
            numbers_list.append(int(word))
    
    # Step 4: Sort the list of numbers in ascending order
    numbers_list.sort()
    
    # Step 5: Create an empty list to store the sorted numbers as strings
    sorted_numbers = []
    
    # Step 6: Iterate through each number in the sorted list
    for number in numbers_list:
        # Convert the number to a string and add it to the list of sorted numbers
        sorted_numbers.append(str(number))
    
    # Step 7: Join the list of sorted numbers with spaces to create the final string
    sorted_numbers_str = ' '.join(sorted_numbers)
    
    # Step 8: Return the sorted string
    return sorted_numbers_str