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
    1. Understand the function parameters:
       - arr: a non-empty array of integers
       - k: an integer representing the number of elements to consider

    2. Limit the array to the first k elements:
       - Use array slicing to consider only the first k elements of arr

    3. Filter elements with at most two digits:
       - For each element in the sliced array:
         a. Convert the element to a string
         b. Check if the length of the string is less than or equal to 2
         c. Keep the element if it satisfies this condition

    4. Sum the filtered elements:
       - Use a method to sum all the elements that passed the filter

    5. Return the calculated sum
    """
    # Step 2: Limit the array to the first k elements
    limited_arr = arr[:k]

    # Step 3: Filter elements with at most two digits
    filtered_arr = [num for num in limited_arr if len(str(num)) <= 2]

    # Step 4: Sum the filtered elements
    sum_of_elements = sum(filtered_arr)

    # Step 5: Return the calculated sum
    return sum_of_elements