from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    

    Action Plan:
    1. Define the function sum_product with a single parameter: numbers (a list of integers)
    2. Initialize two variables: total_sum and total_product
        - total_sum: set to 0 (for empty sum)
        - total_product: set to 1 (for empty product)
    3. Iterate through each number in the input list:
        - Add the current number to total_sum
        - Multiply the current number with total_product
    4. After the iteration, return a tuple containing:
        - total_sum
        - total_product
    5. Consider edge cases:
        - If the input list is empty, return (0, 1) as the result
    6. Test the function with example inputs to ensure correct output"""

    total_sum = 0
    total_product = 1

    for number in numbers:
        total_sum += number
        total_product *= number

    return (total_sum, total_product)