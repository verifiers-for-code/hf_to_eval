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
    1. Check if the input array is empty. If so, return None.
    2. Initialize a variable to store the product of signs. If the array contains a 0, set the product to 0. Otherwise:
       a. Count the number of negative numbers in the array.
       b. Calculate the product of signs by raising -1 to the power of the count of negative numbers.
    3. Calculate the sum of magnitudes of the integers in the array.
    4. Return the product of signs multiplied by the sum of magnitudes."""

    if not arr:
        return None

    product_of_signs = 0
    negative_count = 0

    for num in arr:
        if num == 0:
            product_of_signs = 0
            break
        elif num < 0:
            negative_count += 1

    product_of_signs = (-1) ** negative_count

    sum_of_magnitudes = sum(abs(num) for num in arr)

    return product_of_signs * sum_of_magnitudes