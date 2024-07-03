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
    1. Initialize an empty list to store the final result.
    2. Create a dictionary that maps digits (1-9) to their corresponding names.
    3. Filter the input array to only include integers between 1 and 9 (inclusive).
    4. Sort the filtered array in ascending order and then reverse it.
    5. Iterate through the reversed array:
       a. For each digit, try to find its corresponding name in the dictionary.
       b. If the digit has a corresponding name, add it to the result list.
    6. Return the result list containing the names of the digits."""

    # Step 1: Initialize an empty list to store the final result.
    result = []

    # Step 2: Create a dictionary that maps digits (1-9) to their corresponding names.
    digit_names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Step 3: Filter the input array to only include integers between 1 and 9 (inclusive).
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # Step 4: Sort the filtered array in ascending order and then reverse it.
    sorted_arr = sorted(filtered_arr, reverse=True)

    # Step 5: Iterate through the reversed array:
    for num in sorted_arr:
        # a. For each digit, try to find its corresponding name in the dictionary.
        if num in digit_names:
            # b. If the digit has a corresponding name, add it to the result list.
            result.append(digit_names[num])

    # Step 6: Return the result list containing the names of the digits.
    return result