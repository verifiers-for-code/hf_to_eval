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
    2. Calculate the product of signs:
       a. Check if there's a 0 in the array. If so, the product is 0.
       b. If no 0, count the number of negative numbers.
       c. If the count is odd, the product is -1; otherwise, it's 1.
    3. Calculate the sum of absolute values of all numbers in the array.
    4. Multiply the product of signs by the sum of absolute values.
    5. Return the final result.

    Hints:
    - Use a conditional expression to handle the empty array case.
    - Consider using the 'in' operator to check for 0 in the array.
    - The product of signs can be efficiently calculated using the parity of negative numbers.
    - Use list comprehension or map() to calculate absolute values.
    - Remember that the product of signs is either -1, 0, or 1.
    """
    if not arr:
        return None

    # Check if there's a 0 in the array
    if 0 in arr:
        return 0

    # Count the number of negative numbers
    neg_count = sum(1 for num in arr if num < 0)

    # Calculate the product of signs
    prod_sign = -1 if neg_count % 2 else 1

    # Calculate the sum of absolute values
    sum_abs = sum(abs(num) for num in arr)

    # Multiply the product of signs by the sum of absolute values
    result = prod_sign * sum_abs

    return result