def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    

    1. Initialize an empty list to store the numbers without even digits
       - This list will hold the numbers that pass the even digit check
    
    2. Iterate through each number in the input list:
       a. Convert the current number to a string to easily access its digits
       b. Check if the string representation of the number contains any even digits
          - Use a loop or list comprehension to check each digit (e.g., '2', '4', '6', '8')
          - If any even digit is found, skip to the next iteration
       c. If no even digit is found:
          - Add the original number to the new list
    
    3. Sort the new list in increasing order
       - Use a sorting algorithm or a built-in sorting function to sort the list
    
    4. Return the sorted list of numbers without even digits
    
    Additional implementation details:
    - Use a conditional statement (e.g., if-else) to check for even digits
    - Consider using a set or a dictionary to store the digits of each number for efficient lookups
    - Ensure the function handles empty input lists correctly
    - Use a suitable data structure (e.g., list, set) to store the numbers without even digits"""
    no_even_digits = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            no_even_digits.append(num)
    return sorted(no_even_digits)