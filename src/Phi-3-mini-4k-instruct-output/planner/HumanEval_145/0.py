def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    

    Action Plan:
    1. Define a helper function `sum_of_digits` to calculate the sum of digits for a given number:
        a. Convert the number to a string to access individual digits
        b. Iterate through each digit, convert it back to an integer, and add it to a sum
        c. Return the total sum of digits
    
    2. Define the main function `order_by_points` to sort the input list:
        a. Use the `sorted` function with a custom key function
        b. The key function should return a tuple containing the sum of digits and the original index of the number
        c. The `sorted` function will use this tuple to determine the sorting order
    
    3. Implement the sorting logic:
        a. Use the `enumerate` function to get the original index of each number
        b. Pass the sum of digits and original index to the key function
        c. The `sorted` function will sort the list based on these criteria
    
    4. Return the sorted list:
        a. The `sorted` function will return a new list with the numbers sorted according to the specified criteria
        b. Return this sorted list as the result
    
    Note: Be careful when implementing the helper function and the sorting logic to ensure correct results.
    """
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))