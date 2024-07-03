def get_row(lst, x):
    """
    Given a 2 dimensional data, as a nested lists, which is similar to matrix,
    each row may contain a different number of columns. Find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that each tuple is a coordinate - (row, columns),
    starting with 0. Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.

    :param lst: List of lists containing integers
    :param x: Target integer to search for in the list
    :return: Sorted list of coordinates (tuples) of the target integer
    """
    coordinates = []

    # Step 1: Iterate through each row in the input list of lists
    for i, row in enumerate(lst):
        # Step 2: Check if the target integer is present in the current row
        if x in row:
            # Step 2a: Iterate through each element in the row
            for j, element in enumerate(row):
                # Step 2b: If the element matches the target integer, store the coordinates
                if element == x:
                    coordinates.append((i, j))

    # Step 3: Sort the list of coordinates based on the criteria
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))

    return coordinates