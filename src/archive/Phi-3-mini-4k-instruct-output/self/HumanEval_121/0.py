def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0

    Action Plan:
    1. Iterate through the list with a for loop using indices.
    2. Use an if statement to check if the current index is even by using the modulus operator.
    3. Use another if statement to check if the current element is odd by using the modulus operator on the element.
    4. Accumulate the value of elements that satisfy both conditions.
    5. Return the accumulated sum after iterating through the entire list.

    Consider edge cases where the list's length may be odd, affecting the last element's position."""
    result = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            result += lst[i]
    return result