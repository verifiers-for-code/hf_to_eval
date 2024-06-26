def get_row(lst, x):
    """
    Finds coordinates of the target integer 'x' in a 2D list with varying row lengths,
    and returns them sorted by row and column.
    """
    coordinates = []

    # Step 1: Iterate through the rows and find the coordinates of 'x'
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, j))

    # Step 3: Sort the coordinates list
    coordinates.sort(key=lambda x: (x[0], -x[1]))

    return coordinates