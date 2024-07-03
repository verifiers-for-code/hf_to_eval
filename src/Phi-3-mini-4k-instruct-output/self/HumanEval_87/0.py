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
    
    2. Iterate through the outer list to check each sub-list for the integer x.
    
    3. When the integer x is found:
        a. Iterate through the sub-list to find the first occurrence of x.
        b. Add the coordinate (index, column index) to the list, considering the first column as 0.
    
    4. Once the iteration over the outer list is complete, remove duplicates from the coordinates list.
    
    5. Sort the coordinates primarily by rows (first element of each tuple) and secondarily by columns (second element of each tuple) by using a custom sort function.
        a. Implement a custom sort that prioritizes ascending order of rows and descending order of columns for tuples within the same row.
    
    6. Return the sorted list of coordinates.
    
    7. Edge cases to consider:
        a. Empty list input
        b. No occurrences of x
        c. Lists with empty sub-lists or varying column lengths
    """
    coordinates = []
    for i, sublist in enumerate(lst):
        if x in sublist:
            for j, val in enumerate(sublist):
                if val == x:
                    coordinates.append((i, j))
                    break

    coordinates = list(set(coordinates))  # Remove duplicates
    coordinates.sort(key=lambda x: (x[0], -x[1]))  # Sort by row and then by column in descending order
    return coordinates