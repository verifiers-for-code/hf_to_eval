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
    

    1. Handle the input array:
       - Check if the input array is empty
       - If empty, return None immediately
    
    2. Calculate the product of all signs:
       - Initialize a variable to store the product of signs (e.g., `sign_product`)
       - Iterate through each number in the array:
         a. Check if the number is 0
         b. If 0, set `sign_product` to 0 and break the loop
         c. If the number is positive, set `sign_product` to 1
         d. If the number is negative, set `sign_product` to -1
    
    3. Calculate the sum of magnitudes multiplied by the product of signs:
       - Initialize a variable to store the sum of magnitudes (e.g., `sum_of_magnitudes`)
       - Iterate through each number in the array:
         a. Multiply the number by the `sign_product`
         b. Add the result to `sum_of_magnitudes`
    
    4. Return the `sum_of_magnitudes`
    
    Additional implementation details:
    - Use a loop to iterate through the array
    - Use conditional statements to handle the different cases for each number (0, positive, negative)
    - Use a variable to store the product of signs and update it accordingly
    - Use a variable to store the sum of magnitudes and update it accordingly
    - Ensure that the function handles edge cases correctly (empty array)"""
    
    if not arr:
        return None
    
    sign_product = 1
    sum_of_magnitudes = 0
    
    for num in arr:
        if num == 0:
            sign_product = 0
            break
        elif num > 0:
            sign_product *= 1
        else:
            sign_product *= -1
        
        sum_of_magnitudes += abs(num) * sign_product
    
    return sum_of_magnitudes