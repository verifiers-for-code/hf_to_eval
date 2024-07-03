def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
    Action Plan:
    1. Check the input number 'n' to ensure it is a positive integer:
        - Return False if 'n' is not positive
    
    2. Iterate over a range of possible even numbers starting from 2 until the sum of four even numbers would exceed 'n'
        - For each even number 'even_num' in the range, do the following:
            a. Check that 'even_num' is at most 'n/4' (as we are looking for only 4 even numbers)
            b. Create a loop to find three more distinct even numbers that add up to 'n - even_num'
            c. If three even numbers exist, return True
    
    3. If no valid combination is found after the loop, return False
    """
    if not isinstance(n, int) or n <= 0:
        return False

    for even_num in range(2, (n // 4) + 1, 2):
        remaining_sum = n - even_num
        if remaining_sum % 2 != 0:
            continue

        for i in range(2, remaining_sum // 2 + 1, 2):
            if i == even_num:
                continue
            for j in range(i + 2, remaining_sum // 2 + 1, 2):
                if j == i or j == even_num:
                    continue
                for k in range(j + 2, remaining_sum // 2 + 1, 2):
                    if k == i or k == j or k == even_num:
                        continue
                    if i + j + k == remaining_sum:
                        return True

    return False