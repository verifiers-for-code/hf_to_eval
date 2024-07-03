def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    # Initialize the sum to 0
    sum_odd_even_positions = 0
    
    # Iterate over the list with index
    for i in range(len(lst)):
        # Check if the index is even and the element is odd
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum_odd_even_positions += lst[i]
    
    return sum_odd_even_positions