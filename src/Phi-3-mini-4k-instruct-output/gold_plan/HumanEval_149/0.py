def sorted_list_sum(lst):
    # Step 1: Initialize an empty list to store the filtered strings.
    filtered_list = []

    # Step 2: Iterate through each string in the input list.
    for string in lst:
        # Check if the length of the string is even.
        if len(string) % 2 == 0:
            # If even, add the string to the filtered list.
            filtered_list.append(string)

    # Step 3: Sort the filtered list.
    # First, sort alphabetically to handle ties in length.
    filtered_list.sort()
    # Then, sort by length in ascending order.
    filtered_list.sort(key=len)

    # Step 4: Return the sorted and filtered list.
    return filtered_list