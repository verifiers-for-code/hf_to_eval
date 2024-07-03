def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    

    Action Plan:
    1. Extract the first k elements from the input array.
    2. Initialize a variable to store the sum of the desired elements.
    3. Iterate through the extracted elements:
       a. Convert each element to a string to count the number of digits.
       b. Check if the number of digits is less than or equal to 2.
       c. If the element has at most two digits, add it to the sum.
    4. Return the calculated sum of elements with at most two digits from the first k elements.
    """
    # Extract the first k elements from the input array
    first_k_elements = arr[:k]

    # Initialize a variable to store the sum of the desired elements
    sum_of_elements = 0

    # Iterate through the extracted elements
    for element in first_k_elements:
        # Convert each element to a string to count the number of digits
        num_digits = len(str(element))

        # Check if the number of digits is less than or equal to 2
        if num_digits <= 2:
            # If the element has at most two digits, add it to the sum
            sum_of_elements += element

    # Return the calculated sum of elements with at most two digits from the first k elements
    return sum_of_elements