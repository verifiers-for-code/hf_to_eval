def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Step 1: Check for a base case
    if len(l) < 2:
        return False

    # Step 2: Create a set to hold numbers we've seen
    seen = set()

    # Iterate through the list
    for num in l:
        # Calculate the complement
        target = -num

        # Check if the complement is in the set
        if target in seen:
            return True

        # Add the current number to the set
        seen.add(num)

    # Step 3: Return False if no pair is found
    return False