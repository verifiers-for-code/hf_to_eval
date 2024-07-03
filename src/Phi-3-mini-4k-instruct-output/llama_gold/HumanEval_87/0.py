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
    1. Initialize an empty list to store coordinates.
    2. Iterate through each row (i) in the input list:
       a. Iterate through each element (j) in the current row:
          i. Check if the element is equal to the target value x.
          ii. If it is, create a coordinate tuple (i, j) and add it to the coordinates list.
    3. Sort the coordinates list in two stages:
       a. Sort the coordinates by column index in descending order.
       b. Sort the sorted coordinates by row index in ascending order.
    4. Return the final sorted list of coordinates.
    """
    coordinates = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda x: (-x[1], x[0]))
    return coordinates