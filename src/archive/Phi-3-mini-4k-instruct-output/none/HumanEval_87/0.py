def get_row(lst, x):
    """
    Given a 2 dimensional data, as a nested lists, which is similar to matrix,
    each row may contain a different number of columns. Given lst, and integer x,
    find integers x in the list, and return list of tuples, [(x1, y1), (x2, y2) ...]
    such that each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order. Also, sort coordinates
    of the row by columns in descending order.
    """
    result = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result