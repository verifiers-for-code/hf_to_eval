def will_it_fly(q, w):
    """
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal to the maximum possible weight w.

    :param q: List of integers representing the object
    :param w: Maximum possible weight
    :return: Boolean value indicating if the object will fly or not
    """
    # Check if the list is balanced (palindromic)
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal to the maximum possible weight
        if sum(q) <= w:
            return True
    return False