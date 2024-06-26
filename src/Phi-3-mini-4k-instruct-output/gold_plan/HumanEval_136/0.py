def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)

    Action Plan:
    1. Initialize two variables to store the largest negative and smallest positive integers, both set to None.
    2. Iterate through the input list:
       a. If an element is negative and either larger than the current largest negative or the largest negative is None, update the largest negative.
       b. If an element is positive and either smaller than the current smallest positive or the smallest positive is None, update the smallest positive.
    3. Return a tuple containing the largest negative and smallest positive integers.
    '''
    largest_negative = None
    smallest_positive = None

    for num in lst:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num

    return (largest_negative, smallest_positive)