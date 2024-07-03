def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Step 1: Check if the input number n is even
    if n % 2 != 0:
        return False

    # Step 2: Determine the minimum possible sum of 4 positive even numbers
    min_sum = 4 * 2  # The smallest positive even number is 2, and we need 4 of them

    # Step 3: Check if n is greater than or equal to the minimum sum
    if n < min_sum:
        return False

    # Step 4: Combine the results from steps 1 and 3 using logical AND
    return True