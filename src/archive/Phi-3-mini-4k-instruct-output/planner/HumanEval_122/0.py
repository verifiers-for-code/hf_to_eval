def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Args:
    arr (List[int]): A non-empty list of integers.
    k (int): An integer representing the number of elements to consider from the start of the array.

    Returns:
    int: The sum of elements with at most two digits from the first k elements of arr.

    Constraints:
    1. 1 <= len(arr) <= 100
    2. 1 <= k <= len(arr)
    """
    # Step 1: Extract the first k elements from the array
    first_k_elements = arr[:k]

    # Step 2: Filter elements with at most two digits
    filtered_elements = [element for element in first_k_elements if len(str(element)) <= 2]

    # Step 3: Calculate the sum of the filtered elements
    result = sum(filtered_elements)

    # Step 4: Return the final result
    return result