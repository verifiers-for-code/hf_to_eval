def count_digits(num):
    """
    Helper function to count the number of digits in an integer.

    Args:
        num (int): The integer to count digits for.

    Returns:
        int: The number of digits in the integer.
    """
    return len(str(num))


def filter_elements(arr):
    """
    Helper function to filter elements with at most two digits.

    Args:
        arr (list): The list of integers to filter.

    Returns:
        list: A new list with elements that have at most two digits.
    """
    return list(filter(lambda x: count_digits(x) <= 2, arr))


def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Args:
        arr (list): The list of integers.
        k (int): The number of elements to consider from the start of the list.

    Returns:
        int: The sum of the elements with at most two digits from the first k elements.

    Raises:
        ValueError: If k is greater than the length of the array or if the array is empty.
    """
    if not arr:
        raise ValueError("The input array is empty.")
    if k > len(arr):
        raise ValueError("k is greater than the length of the array.")

    filtered_elements = filter_elements(arr[:k])
    return sum(filtered_elements)