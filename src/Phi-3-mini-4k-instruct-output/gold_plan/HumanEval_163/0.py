def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []

    Action Plan:
    1. Determine the lower and upper bounds:
       - Consider that a and b can be in any order
       - The lower bound should be the smaller of a and b, but not less than 2
       - The upper bound should be the larger of a and b, but not more than 8
       - Hint: Use min() and max() functions to handle this logic

    2. Generate a list of even integers:
       - Create a list comprehension that:
         a. Iterates through the range from the lower bound to the upper bound (inclusive)
         b. Includes only even numbers in the result
       - Hint: Use the modulo operator (%) to check for even numbers

    3. Return the resulting list

    Remember to handle edge cases where there might be no even digits in the given range.
    """
    lower_bound = max(2, min(a, b))
    upper_bound = min(8, max(a, b))
    even_integers = [i for i in range(lower_bound, upper_bound + 1) if i % 2 == 0]
    return even_integers