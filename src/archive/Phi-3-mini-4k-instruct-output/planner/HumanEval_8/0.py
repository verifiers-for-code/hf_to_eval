from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)

    Action Plan:
    1. Check if the input list is empty:
        - If empty, return (0, 1) as the sum and product
    2. Initialize variables:
        - Initialize sum to 0
        - Initialize product to 1
    3. Iterate through the input list:
        - For each number in the list:
            a. Add the number to the sum
            b. Multiply the product by the number
    4. Return the final result as a tuple:
        - Return a tuple containing the sum and product

    Note: Use a for loop to iterate through the input list.
    Be careful to initialize the sum and product correctly."""

    if not numbers:  # Check if the input list is empty
        return (0, 1)

    sum_numbers = 0  # Initialize sum to 0
    product_numbers = 1  # Initialize product to 1

    for number in numbers:  # Iterate through the input list
        sum_numbers += number  # Add the number to the sum
        product_numbers *= number  # Multiply the product by the number

    return (sum_numbers, product_numbers)  # Return the final result as a tuple