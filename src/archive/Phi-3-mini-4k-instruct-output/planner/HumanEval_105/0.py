def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
    If the array is empty, return an empty array:
      arr = []
      return []
    
    If the array has any strange number ignore it:
    arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
    return = ['One']

    Action Plan:
    1. Initialize an empty list to store the filtered numbers.
    2. Iterate through the input array:
        a. Check if the current number is between 1 and 9 (inclusive).
        b. If it is, add the number to the filtered list.
    3. Sort the filtered list in descending order.
    4. Initialize an empty list to store the final result.
    5. Iterate through the sorted list:
        a. For each number, replace it with its corresponding name from "One" to "Nine".
        b. Add the name to the result list.
    6. Return the result list.
    
    Note: Handle edge cases:
    - If the input array is empty, return an empty array.
    - If the input array contains numbers outside the range of 1 to 9, ignore them and continue with the remaining numbers."""
    
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    # Step 1
    filtered_nums = [num for num in arr if 1 <= num <= 9]
    
    # Step 2
    filtered_nums.sort(reverse=True)
    
    # Step 3
    result = []
    
    # Step 5
    for num in filtered_nums:
        result.append(digit_names[num - 1])
    
    return result