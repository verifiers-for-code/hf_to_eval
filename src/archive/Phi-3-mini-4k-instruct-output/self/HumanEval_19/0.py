from typing import List

def sort_numbers(numbers: str) -> str:
    # Step 1: Split the string into a list of words using `split()`
    words = numbers.split()
    
    # Step 2: Validate each word to ensure it's a valid number ('zero' to 'nine')
    valid_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    valid_words = []
    
    for word in words:
        if word in valid_numbers:
            valid_words.append(word)
        else:
            return "Invalid input: only 'zero' to 'nine' are allowed."
    
    # Step 3: Convert valid words to integers and store them in a new list
    numbers_list = [int(word) for word in valid_words]
    
    # Step 4: Sort the list of integers
    numbers_list.sort()
    
    # Step 5: Create a new list of words by mapping each integer back to its corresponding string
    sorted_words = [valid_numbers[num] for num in numbers_list]
    
    # Step 6: Join the list of words into a single string with spaces in between
    sorted_numbers = ' '.join(sorted_words)
    
    # Step 7: Edge case considerations
    # a. Return the sorted string if all inputs are valid
    return sorted_numbers