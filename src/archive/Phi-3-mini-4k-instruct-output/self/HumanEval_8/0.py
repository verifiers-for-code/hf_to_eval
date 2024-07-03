from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Step 1: Initialize sum and product variables
    sum_val = 0
    product_val = 1

    # Step 2: Iterate through the input list with a for loop
    for num in numbers:
        sum_val += num
        product_val *= num

    # Step 3: After the loop, return a tuple (sum, product)
    return (sum_val, product_val)

# Step 4: Handle an empty list
if __name__ == "__main__":
    print(sum_product([]))  # Output: (0, 1)
    print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)

# Step 5: Consider other edge cases
# This function already handles the edge case of an empty list.
# For lists containing zeros, the product will be zero, which is correct.
# For lists containing negative numbers, the sum and product will be calculated correctly.

# Step 6: Discuss potential optimizations
# While using `itertools.accumulate()` and `functools.reduce()` could optimize the code,
# the provided solution is straightforward and easy to understand.
# However, if performance is a concern, these functions can be used as follows:

# from itertools import accumulate
# from functools import reduce

# def sum_product_optimized(numbers: List[int]) -> Tuple[int, int]:
#     sum_val = reduce(lambda x, y: x + y, numbers, 0)
#     product_val = reduce(lambda x, y: x * y, numbers, 1)
#     return (sum_val, product_val)