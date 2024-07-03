def get_row(lst, x):
    """
    Finds coordinates of integer x in a 2D list and returns them sorted by rows and columns.
    """
    # Step 1: Initialize an empty list to store the coordinates.
    coordinates = []

    # Step 2: Iterate through the outer list to check each sub-list for the integer x.
    for i, sub_list in enumerate(lst):
        # Step 3a: Iterate through the sub-list to find the first occurrence of x.
        for j, value in enumerate(sub_list):
            if value == x:
                # Step 3b: Add the coordinate (index, column index) to the list.
                coordinates.append((i, j))
                break  # Break the inner loop to avoid adding duplicate coordinates.

    # Step 4: Remove duplicates from the coordinates list.
    coordinates = list(set(coordinates))

    # Step 5: Sort the coordinates primarily by rows and secondarily by columns.
    coordinates.sort(key=lambda x: (x[0], -x[1]))

    return coordinates