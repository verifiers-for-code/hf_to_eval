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
    1. Determine the product of signs:
        - Set a variable for the product of signs, initialized to 1
        - Iterate through the input array, updating the product of signs
          - If the sign of the current element is 0, skip it
          - If the sign is positive, multiply by 1
          - If the sign is negative, multiply by -1
    
    2. Separate positive and negative elements:
        - Create two lists, one for positive numbers and one for negative numbers
        - Iterate over the input array, appending non-zero numbers to their respective lists
    
    3. Calculate the product of magnitudes:
        - Initialize two variables for the product of positives and negatives, both starting at 1
        - Iterate over the positive numbers list, multiplying each magnitude
        - Iterate over the negative numbers list, multiplying each magnitude (remembering they're negative, so use absolute value)
    
    4. Calculate the sum of products:
        - Add the product of magnitudes of positives to the product of magnitudes of negatives
    
    5. Handle edge cases:
        - If the input array is empty, return None
        - If the array contains only zeroes, return 0 since the product of signs and magnitudes would be zero
    
    6. Return the computed sum
    """
    if not arr:
        return None
    
    product_of_signs = 1
    for num in arr:
        if num == 0:
            continue
        product_of_signs *= -1 if num < 0 else 1
    
    positives = [abs(num) for num in arr if num > 0]
    negatives = [abs(num) for num in arr if num < 0]
    
    product_of_positives = 1
    for num in positives:
        product_of_positives *= num
    
    product_of_negatives = 1
    for num in negatives:
        product_of_negatives *= num
    
    return product_of_positives * product_of_negatives * product_of_signs