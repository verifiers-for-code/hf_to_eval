def get_row(lst, x):
    """
    Given a 2 dimensional data, as a nested lists, and an integer x,
    find integers x in the list, and return list of tuples,
    [(x1, y1), (x2, y2) ...] such that each tuple is a coordinate - (row, columns),
    starting with 0. Sort coordinates initially by rows in ascending order,
    and sort coordinates of the row by columns in descending order.
    """
    coordinates = []

    # Step 1: Iterate through the rows of the input list 'lst'
    for i, row in enumerate(lst):
        # Step 2: Iterate through the elements in the current row
        for j, element in enumerate(row):
            # Step 2b: If the element equals the target value 'x'
            if element == x:
                # Append the tuple (i, j) to the coordinates list
                coordinates.append((i, j))

    # Step 3: Sort the coordinates list
    coordinates.sort(key=lambda x: (x[0], -x[1]))

    return coordinates