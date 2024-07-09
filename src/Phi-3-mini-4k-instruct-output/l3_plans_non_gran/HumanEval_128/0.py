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
        - If empty, return None
    
    2. Initialize two variables:
        - `sign_product` to store the product of all signs in the array (initially 1)
        - `sum_magnitudes` to store the sum of magnitudes of integers in the array (initially 0)
    
    3. Iterate through each element in the input array:
        - For each element, update `sign_product` based on its sign:
            - If the element is positive, multiply `sign_product` by 1
            - If the element is negative, multiply `sign_product` by -1
            - If the element is zero, leave `sign_product` unchanged
        - Add the magnitude of the current element to `sum_magnitudes`
    
    4. After iterating through the entire array, calculate the final result:
        - Multiply `sum_magnitudes` by `sign_product`
    
    5. Return the final result
    """
    if not arr:
        return None
    
    sign_product = 1
    sum_magnitudes = 0
    
    for num in arr:
        if num > 0:
            sign_product *= 1
        elif num < 0:
            sign_product *= -1
        # If num is 0, sign_product remains unchanged
        
        sum_magnitudes += abs(num)
    
    return sum_magnitudes * sign_product