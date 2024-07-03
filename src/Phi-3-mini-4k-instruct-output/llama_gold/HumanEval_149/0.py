def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    

    Action Plan:
    1. Initialize an empty list to store the filtered strings.
    2. Iterate through the input list of strings:
       a. Check if the length of the current string is even.
       b. If it's even, add the string to the new list.
    3. Sort the new list of strings based on two criteria:
       a. Primary sort criterion: the length of each string (in ascending order).
       b. Secondary sort criterion: alphabetical order (in case of ties).
    4. Return the sorted list of strings."""

    # Step 1: Initialize an empty list to store the filtered strings.
    filtered_list = []

    # Step 2: Iterate through the input list of strings.
    for word in lst:
        # Check if the length of the current string is even.
        if len(word) % 2 == 0:
            # If it's even, add the string to the new list.
            filtered_list.append(word)

    # Step 3: Sort the new list of strings based on two criteria.
    # Primary sort criterion: the length of each string (in ascending order).
    # Secondary sort criterion: alphabetical order (in case of ties).
    filtered_list.sort(key=lambda x: (len(x), x))

    # Step 4: Return the sorted list of strings.
    return filtered_list