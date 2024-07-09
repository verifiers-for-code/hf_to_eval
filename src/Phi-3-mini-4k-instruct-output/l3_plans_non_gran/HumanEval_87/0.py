def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    

    Action Plan:
    1. Initialize an empty list to store the coordinates of x.
    2. Iterate through each row in the input list:
        a. Check if x is present in the current row.
        b. If x is found, find its index in the row.
        c. Append the coordinate (row index, column index) to the list of coordinates.
    3. Sort the list of coordinates based on two criteria:
        a. Sort by row index in ascending order.
        b. For each row, sort by column index in descending order.
    4. Return the sorted list of coordinates.
    
    Note: Use appropriate list methods for finding the index of x and sorting the coordinates.
    Be careful when sorting the coordinates to ensure the correct order."""
    
    coordinates = []
    for i, row in enumerate(lst):
        if x in row:
            index = row.index(x)
            coordinates.append((i, index))
    
    coordinates.sort(key=lambda x: (x[0], -x[1]))
    return coordinates