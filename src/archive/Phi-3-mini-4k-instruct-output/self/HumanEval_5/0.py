from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`."""
    # Step 1: Initialize a new list, `interspersed_numbers`
    interspersed_numbers = []

    # Step 2: Iterate over `numbers` using a for loop and `enumerate` to get both index and value
    for index, value in enumerate(numbers):
        # Step 3: Check if the current index is not the last index
        if index != len(numbers) - 1:
            # Append the delimeter followed by the current value to `interspersed_numbers`
            interspersed_numbers.append(delimeter)
            interspersed_numbers.append(value)
        else:
            # If false, append the current value to `interspersed_numbers`
            interspersed_numbers.append(value)

    # Step 4: After the loop, return `interspersed_numbers`
    return interspersed_numbers