def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1

    Action Plan:
    1. Create a frequency counter:
       - Determine the maximum value in the input list to set the range of the frequency counter.
       - Initialize a list to store the frequency of each number, with index representing the number itself.

    2. Count the frequencies:
       - Iterate through the input list.
       - For each number, increment its count in the frequency counter.

    3. Find the greatest valid integer:
       - Initialize a variable to store the answer, starting with -1 (in case no valid integer is found).
       - Iterate through the range from 1 to the maximum value (inclusive):
         - Check if the current number's frequency is greater than or equal to the number itself.
         - If true, update the answer variable with this number.

    4. Return the result:
       - After the iteration, return the answer variable.
       - If no valid integer was found, this will return -1 as initialized.
    '''
    # Step 1: Create a frequency counter
    max_val = max(lst)
    freq_counter = [0] * (max_val + 1)

    # Step 2: Count the frequencies
    for num in lst:
        freq_counter[num] += 1

    # Step 3: Find the greatest valid integer
    answer = -1
    for i in range(1, max_val + 1):
        if freq_counter[i] >= i:
            answer = i

    # Step 4: Return the result
    return answer