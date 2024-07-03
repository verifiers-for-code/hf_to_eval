def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    :param arr: a non-empty array of integers
    :param k: an integer representing the number of elements to consider
    :return: the sum of the elements with at most two digits from the first k elements of arr
    """
    # Step 1: Limit the array to the first k elements
    limited_arr = arr[:k]

    # Step 2: Filter elements with at most two digits
    filtered_elements = [element for element in limited_arr if len(str(element)) <= 2]

    # Step 4: Sum the filtered elements
    result = sum(filtered_elements)

    # Step 5: Return the calculated sum
    return result