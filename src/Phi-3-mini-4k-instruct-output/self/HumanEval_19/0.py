from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
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
    
    8. Test the function with various input scenarios, including the provided examples
    """
    # Step 1: Split the string into a list of words
    words = numbers.split()
    
    # Step 2: Validate each word
    valid_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    valid_words = [word for word in words if word in valid_numbers]
    
    # Step 3: Convert valid words to integers
    try:
        numbers_list = [int(word) for word in valid_words]
    except ValueError:
        return "Invalid input: all elements must be valid numbers ('zero' to 'nine')"
    
    # Step 4: Sort the list of integers
    numbers_list.sort()
    
    # Step 5: Create a new list of words by mapping each integer back to its corresponding string
    sorted_words = [valid_numbers[num] for num in numbers_list]
    
    # Step 6: Join the list of words into a single string with spaces in between
    sorted_string = ' '.join(sorted_words)
    
    # Step 7: Edge case considerations
    # a. Return the sorted string if all inputs are valid
    # b. Handle cases with non-numeric or out-of-range elements
    # c. Return an appropriate message or error for invalid input
    
    # Step 8: Test the function with various input scenarios, including the provided examples
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('nine eight seven six') == 'eight nine seven six'
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('zero one two three four five six seven eight nine ten') == "Invalid input: all elements must be valid numbers ('zero' to 'nine')"
    assert sort_numbers('zero one two three four five six seven eight nine one') == "Invalid input: all elements must be valid numbers ('zero' to 'nine')"
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('') == ""
    assert sort_numbers('zero one two three four five six seven eight nine one two three four five six seven eight nine ten') == "Invalid input: all elements must be valid numbers ('zero' to 'nine')"
    assert sort_numbers('zero one two three four five six seven eight nine one two three four five six seven eight nine one two three four five six seven eight nine ten') == "Invalid input: all elements must be valid numbers ('zero' to 'nine')"
    
    return sorted_string