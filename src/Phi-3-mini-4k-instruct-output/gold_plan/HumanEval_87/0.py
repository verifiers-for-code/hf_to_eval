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
    1. Initialize an empty list to store the coordinates.
    2. Iterate through the rows of the input list 'lst':
       a. For each row, get its index (i).
       b. Iterate through the elements in the current row:
          i. For each element, get its index (j).
          ii. If the element equals the target value 'x':
              - Append the tuple (i, j) to the coordinates list.
    3. Sort the coordinates list:
       a. First, sort by row (first element of each tuple) in ascending order.
       b. Then, sort by column (second element of each tuple) in descending order.
    4. Return the sorted coordinates list.

    Note: Implement the sorting in step 3 using Python's built-in sorting 
    functions with appropriate key functions and reverse parameters.
    """
    coordinates = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    coordinates.sort(key=lambda x: (x[0], -x[1]))
    return coordinates