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
    
    1. Initialize an empty list to store the coordinates of the found elements
       - This list will hold tuples in the format (row, column)
    
    2. Iterate through each row in the input list:
       a. Iterate through each element in the current row:
          - Check if the element is equal to the specified integer x
          - If it is, append the coordinates (row, column) to the list
          - Use enumerate to keep track of the row and column indices
    
    3. Sort the list of coordinates:
       - Use the sorted function with a lambda function as the key
       - Sort by rows in ascending order (first element of the tuple)
       - Then sort by columns in descending order (second element of the tuple)
    
    4. Return the sorted list of coordinates
    
    Additional implementation details:
    - Use a nested loop to iterate through the 2D list
    - Use enumerate to keep track of the row and column indices
    - Use the sorted function with a lambda function as the key to sort the list
    - Ensure that the function handles empty input lists and edge cases correctly
    - Consider using a list comprehension or generator expression for a more concise implementation
    """
    coordinates = [(row, col) for row, lst in enumerate(lst) for col, val in enumerate(lst) if val == x]
    return sorted(coordinates, key=lambda x: (x[0], -x[1]))