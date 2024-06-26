def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Action Plan:
    1. Initialize a variable to store the sum, starting at 0.
    2. Iterate through the list using enumeration to access both index and value.
    3. For each element:
       a. Check if its position is even (index % 2 == 0).
       b. If so, check if the element itself is odd (element % 2 == 1).
       c. If both conditions are true, add the element to the sum.
    4. After the iteration, return the final sum.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    sum_odd_even_positions = 0
    for index, value in enumerate(lst):
        if index % 2 == 0 and value % 2 == 1:
            sum_odd_even_positions += value
    return sum_odd_even_positions