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
    1. Initialize an empty list to store the coordinates of the target integer.
    2. Iterate through each row in the input list of lists:
        a. Check if the target integer is present in the current row.
        b. If found, iterate through each element in the row:
            - If the element matches the target integer, store the coordinates (row, column) in the list.
    3. Sort the list of coordinates based on the following criteria:
        a. Sort by rows in ascending order.
        b. Sort by columns in descending order within each row.
    4. Return the sorted list of coordinates.
    
    Note: Use appropriate list methods for iteration, checking, and sorting.
    Be careful when handling the nested list structure and coordinate storage.
    """
    coordinates = []
    for row_index, row in enumerate(lst):
        for col_index, element in enumerate(row):
            if element == x:
                coordinates.append((row_index, col_index))
    coordinates.sort(key=lambda x: (x[0], -x[1]))
    return coordinates