from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    

    Action Plan:
    1. Initialize two variables: one for the sum (with a default value of 0) and one for the product (with a default value of 1).
    2. Iterate through each number in the input list:
       a. Add the current number to the sum variable.
       b. Multiply the current number with the product variable.
    3. After iterating through all numbers, return a tuple containing the final sum and product values."""
    
    # Step 1: Initialize sum and product variables
    sum_val = 0
    product_val = 1
    
    # Step 2: Iterate through each number in the input list
    for num in numbers:
        sum_val += num
        product_val *= num
    
    # Step 3: Return a tuple containing the final sum and product values
    return (sum_val, product_val)