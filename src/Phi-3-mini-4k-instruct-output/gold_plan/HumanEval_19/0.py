from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'

    Action Plan:
    1. Create a dictionary to map word representations of numbers to their integer values.
       This will be used for sorting later.

    2. Split the input string into a list of individual words.
       Hint: Use the split() method with a space delimiter.

    3. Sort the list of words:
       a. Use the sorted() function with a custom key.
       b. The key should be a lambda function that maps each word to its corresponding integer value using the dictionary from step 1.

    4. Join the sorted list of words back into a string.
       Hint: Use the join() method with a space separator.

    5. Return the resulting sorted string.
    """

    # Step 1: Create a dictionary to map word representations of numbers to their integer values.
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

    # Step 2: Split the input string into a list of individual words.
    words = numbers.split()

    # Step 3: Sort the list of words.
    sorted_words = sorted(words, key=lambda word: number_dict[word])

    # Step 4: Join the sorted list of words back into a string.
    sorted_numbers = ' '.join(sorted_words)

    # Step 5: Return the resulting sorted string.
    return sorted_numbers