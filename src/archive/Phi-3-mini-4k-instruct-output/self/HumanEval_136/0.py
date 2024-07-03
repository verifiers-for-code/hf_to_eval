def largest_smallest_integers(lst):
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    # Initialize variables to store the largest negative integer and smallest positive integer
    largest_negative = None
    smallest_positive = None

    # Iterate through the list
    for num in lst:
        # Check if the number is negative
        if num < 0:
            # Update largest_negative if the current number is larger
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        # Check if the number is positive
        elif num > 0:
            # Update smallest_positive if the current number is smaller
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num

    # Return the tuple (largest_negative, smallest_positive)
    return (largest_negative, smallest_positive)