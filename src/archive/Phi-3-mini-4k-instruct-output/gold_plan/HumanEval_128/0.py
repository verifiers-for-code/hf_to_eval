def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.
    """
    # Step 1: Check if the input array is empty. If so, return None.
    if not arr:
        return None

    # Step 2: Calculate the product of signs
    has_zero = 0 in arr
    negatives = sum(1 for num in arr if num < 0)
    product_of_signs = -1 if negatives % 2 else 1 if not has_zero else 0

    # Step 3: Calculate the sum of absolute values of all numbers in the array
    sum_of_abs_values = sum(abs(num) for num in arr)

    # Step 4: Multiply the product of signs by the sum of absolute values
    result = product_of_signs * sum_of_abs_values

    # Step 5: Return the final result
    return result