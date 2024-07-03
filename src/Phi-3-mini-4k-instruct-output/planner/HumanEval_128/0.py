def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    

    Action Plan:
    1. Check if the input array is empty:
        - If true, return None
    2. Initialize two variables:
        - `sign_product` to store the product of signs (1, -1, or 0)
        - `magnitude_sum` to store the sum of magnitudes of integers
    3. Iterate through each number in the array:
        - Calculate the sign of the current number (1, -1, or 0)
        - Update `sign_product` by multiplying it with the current sign
        - Calculate the magnitude of the current number (absolute value)
        - Update `magnitude_sum` by adding the magnitude to it
    4. Return the product of `sign_product` and `magnitude_sum`
    
    Note: Use appropriate mathematical operations and conditional statements to implement the logic.
    Be careful with the handling of edge cases and the calculation of the product of signs and sum of magnitudes.
    """
    if not arr:
        return None
    
    sign_product = 1
    magnitude_sum = 0
    
    for num in arr:
        sign = 1 if num > 0 else -1 if num < 0 else 0
        sign_product *= sign
        magnitude_sum += abs(num)
    
    return sign_product * magnitude_sum