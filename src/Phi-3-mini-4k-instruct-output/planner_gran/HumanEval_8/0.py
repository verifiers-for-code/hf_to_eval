from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
    1. Check if the input list is empty:
       - Use a conditional statement to check if the list is empty
       - If the list is empty, return a tuple with 0 and 1 as the sum and product, respectively
    
    2. Calculate the sum of the integers in the list:
       - Use the built-in sum() function to calculate the sum of the integers
    
    3. Calculate the product of the integers in the list:
       - Initialize a variable to store the product (e.g., product = 1)
       - Iterate through each integer in the list
       - Multiply the current product by the current integer
    
    4. Return the result as a tuple:
       - Create a tuple with the calculated sum and product
       - Return the tuple as the result of the function
    
    Additional implementation details:
    - Use the appropriate data type for the input list (e.g., List[int])
    - Use a descriptive variable name for the product (e.g., product)
    - Consider adding a docstring to explain the function's purpose, parameters, and return value
    - Ensure the function handles edge cases, such as an empty list or a list with a single element"""
    if not numbers:
        return (0, 1)
    else:
        sum_of_numbers = sum(numbers)
        product_of_numbers = 1
        for num in numbers:
            product_of_numbers *= num
        return (sum_of_numbers, product_of_numbers)