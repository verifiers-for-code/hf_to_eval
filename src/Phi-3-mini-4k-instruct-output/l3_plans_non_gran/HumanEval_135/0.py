def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    

    Action Plan:
    1. Initialize an empty dictionary (frequency counter) to store the frequency of each element in the array.
    2. Iterate through the array and populate the frequency counter:
        - For each element, increment its count in the frequency counter if it already exists.
        - If the element is not in the frequency counter, add it with a count of 1.
    3. Initialize a variable to store the largest index that satisfies the condition (initially -1).
    4. Iterate through the frequency counter in reverse order:
        - For each element, check if its count is greater than 1.
        - If the count is greater than 1, update the largest index variable with the current index.
    5. Return the largest index that satisfies the condition. If no such element exists, return -1."""

    # Step 1: Initialize an empty dictionary (frequency counter)
    freq_counter = {}

    # Step 2: Populate the frequency counter
    for i, num in enumerate(arr):
        if num in freq_counter:
            freq_counter[num] += 1
        else:
            freq_counter[num] = 1

    # Step 3: Initialize a variable to store the largest index
    largest_index = -1

    # Step 4: Iterate through the frequency counter in reverse order
    for num, count in reversed(freq_counter.items()):
        if count > 1:
            largest_index = len(arr) - 1 - arr[::-1].index(num)
            break

    # Step 5: Return the largest index
    return largest_index