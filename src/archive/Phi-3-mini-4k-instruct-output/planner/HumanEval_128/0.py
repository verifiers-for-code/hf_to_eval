def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Parameters:
    arr (list): A list of integers

    Returns:
    int or None: The product of magnitudes of integers multiplied by product of all signs
    """
    if not arr:  # Check if the input array is empty
        return None

    sign_product = 1  # Initialize sign_product to store the product of signs
    magnitude_sum = 0  # Initialize magnitude_sum to store the sum of magnitudes

    for num in arr:
        sign = 1 if num >= 0 else -1  # Calculate the sign of the current number
        sign_product *= sign  # Update sign_product by multiplying it with the current sign
        magnitude_sum += abs(num)  # Update magnitude_sum by adding the magnitude to it

    return sign_product * magnitude_sum  # Return the product of sign_product and magnitude_sum