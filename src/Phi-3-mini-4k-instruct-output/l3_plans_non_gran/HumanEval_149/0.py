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
    1. Create a new list to store the strings with even lengths.
    2. Iterate through each string in the input list:
        a. Check if the length of the string is even.
        b. If the length is even, add the string to the new list.
    3. Sort the new list of strings based on two criteria:
        a. The length of each string (ascending order)
        b. The alphabetical order of each string (in case of equal length)
    4. Return the sorted list of strings.
    
    Note: Use appropriate list methods for filtering, sorting, and indexing.
    Be careful when handling edge cases, such as an empty input list or a list with only one element."""
    
    # Step 1: Create a new list to store the strings with even lengths
    even_length_strings = []
    
    # Step 2: Iterate through each string in the input list
    for string in lst:
        # Check if the length of the string is even
        if len(string) % 2 == 0:
            # If the length is even, add the string to the new list
            even_length_strings.append(string)
    
    # Step 3: Sort the new list of strings based on two criteria
    # The sorting is done using the sorted() function with a custom key
    # The key is a lambda function that returns a tuple with the length of the string and the string itself
    # This ensures that the list is sorted first by length (ascending order) and then alphabetically (in case of equal length)
    sorted_strings = sorted(even_length_strings, key=lambda x: (len(x), x))
    
    # Step 4: Return the sorted list of strings
    return sorted_strings