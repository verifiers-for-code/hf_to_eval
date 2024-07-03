from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
    Action Plan:
    1. Initialize two variables:
       - One for the sum, starting at 0
       - One for the product, starting at 1
    2. Iterate through each number in the input list
    3. For each number:
       - Add it to the sum variable
       - Multiply it with the product variable
    4. After the iteration, return a tuple containing:
       - The final sum value
       - The final product value
    """
    sum_val = 0
    product_val = 1
    for num in numbers:
        sum_val += num
        product_val *= num
    return (sum_val, product_val)