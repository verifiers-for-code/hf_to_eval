
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2
    """
    # Initialize the sum to 0
    sum_even_at_odd_indices = 0

    # Iterate over the list with index
    for i in range(len(lst)):
        # Check if the index is odd and the element is even
        if i % 2 != 0 and lst[i] % 2 == 0:
            sum_even_at_odd_indices += lst[i]

    return sum_even_at_odd_indices