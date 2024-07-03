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
       b. If even, add the string to the filtered list.
    3. Sort the filtered list:
       a. First, sort alphabetically to handle ties in length.
       b. Then, sort by length in ascending order.
    4. Return the sorted and filtered list.
    """
    filtered_list = []
    for word in lst:
        if len(word) % 2 == 0:
            filtered_list.append(word)
    filtered_list.sort()
    filtered_list.sort(key=len)
    return filtered_list