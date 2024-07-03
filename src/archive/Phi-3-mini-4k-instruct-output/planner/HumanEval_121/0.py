def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0

    Action Plan:
    1. Initialize a variable `sum_odd_even` to store the sum of odd elements in even positions.
    2. Iterate through the input list `lst` with a step of 2 (i.e., `lst[::2]`).
    3. For each element in the list:
        a. Check if the element is odd (i.e., `element % 2!= 0`).
        b. If the element is odd, add it to `sum_odd_even`.
    4. After iterating through the entire list, return the final value of `sum_odd_even`.

    Note: Use the modulo operator (`%`) to check if an element is odd.
    Be careful when iterating through the list with a step of 2 to ensure you're only considering even positions."""
    sum_odd_even = 0
    for element in lst[::2]:
        if element % 2 != 0:
            sum_odd_even += element
    return sum_odd_even