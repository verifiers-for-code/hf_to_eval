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
    2. Iterate through each string in the input list:
        a. Check if the length of the string is even.
        b. If the length is even, add the string to the filtered list.
    3. Sort the filtered list:
        a. Use a sorting algorithm that can handle multiple sorting criteria (length and alphabetical order).
        b. Implement a custom sorting function that compares strings based on their lengths and alphabetical order.
        c. Use a stable sorting algorithm to maintain the original order of strings with the same length.
    4. Return the sorted list of strings.
    
    Note: Consider using Python's built-in sorting functions or libraries to simplify the implementation.
    Be careful when implementing the custom sorting function to handle the multiple sorting criteria correctly."""

    # Step 1: Initialize an empty list to store the filtered strings.
    filtered_list = []

    # Step 2: Iterate through each string in the input list.
    for string in lst:
        # Check if the length of the string is even.
        if len(string) % 2 == 0:
            # If the length is even, add the string to the filtered list.
            filtered_list.append(string)

    # Step 3: Sort the filtered list.
    # Use Python's built-in sorted function with a custom key function.
    # The key function returns a tuple with the length of the string and the string itself.
    # This ensures that the list is sorted by length first, and then alphabetically for strings with the same length.
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))

    # Step 4: Return the sorted list of strings.
    return sorted_list