def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    

    Action Plan:
    1. Begin by rounding each number in the list to the nearest integer using the `int()` function applied to the ceiling value.
    
    2. Create a list of squared numbers using list comprehension:
        - Apply the squaring operation to each number in the modified list (where each number is rounded and converted to an integer first).
    
    3. Sum the squared numbers:
        - Use the built-in `sum()` function to add up all the squared values in the list.
    
    4. Consider edge cases:
        a. Empty input list
        b. List with all negative numbers
        c. List with non-integer values (ensure that the rounding process works as intended)
    
    5. Optimize where possible:
        - You can optimize by combining steps 2 and 3 into a single list comprehension statement.
    
    6. Verify with the provided test cases and additional edge cases."""
    
    # Step 1: Round each number to the nearest integer
    rounded_lst = [int(x) for x in lst]
    
    # Step 2 & 3: Create a list of squared numbers and sum them
    sum_of_squares = sum([x**2 for x in rounded_lst])
    
    return sum_of_squares