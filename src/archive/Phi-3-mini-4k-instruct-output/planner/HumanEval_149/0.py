def sorted_list_sum(lst):
    """
    Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word,
    and you should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.

    Action Plan:
    1. Initialize an empty list to store the filtered strings.
    2. Iterate through each string in the input list:
        a. Check if the length of the string is even.
        b. If the length is even, add the string to the filtered list.
    3. Sort the filtered list:
        a. Use Python's built-in sorting function with a custom key function.
        b. Implement a custom sorting function that compares strings based on their lengths and alphabetical order.
        c. Use a stable sorting algorithm to maintain the original order of strings with the same length.
    4. Return the sorted list of strings.
    """
    # Step 1: Initialize an empty list to store the filtered strings
    filtered_list = [word for word in lst if len(word) % 2 == 0]

    # Step 3: Sort the filtered list using Python's built-in sorting function with a custom key function
    filtered_list.sort(key=lambda x: (len(x), x))

    return filtered_list