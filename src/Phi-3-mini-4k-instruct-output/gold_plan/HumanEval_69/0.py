def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Step 1: Create a frequency counter
    max_val = max(lst)
    freq_counter = [0] * (max_val + 1)

    # Step 2: Count the frequencies
    for num in lst:
        freq_counter[num] += 1

    # Step 3: Find the greatest valid integer
    result = -1
    for num in range(1, max_val + 1):
        if freq_counter[num] >= num:
            result = num

    # Step 4: Return the result
    return result