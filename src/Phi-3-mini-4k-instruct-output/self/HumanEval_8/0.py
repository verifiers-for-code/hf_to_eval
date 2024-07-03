from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    

    Action Plan:
    1. Initialize sum and product variables:
        - sum = 0
        - product = 1
    
    2. Iterate through the input list with a for loop:
        - Add each number to the sum
        - Multiply each number with the product
    
    3. After the loop, return a tuple (sum, product)
    
    4. Handle an empty list:
        - If the input list is empty, return (0, 1)
    
    5. Consider other edge cases (e.g., a list containing zeros or negative numbers)
    
    6. Discuss potential optimizations, such as using `itertools.accumulate()` for sum and reduce for product. However, avoid suggesting library functions that might obscure the logic being implemented."""
    
    # Initialize sum and product variables
    sum_val = 0
    product_val = 1
    
    # Iterate through the input list with a for loop
    for num in numbers:
        sum_val += num
        product_val *= num
    
    # Return a tuple (sum, product)
    return (sum_val, product_val)