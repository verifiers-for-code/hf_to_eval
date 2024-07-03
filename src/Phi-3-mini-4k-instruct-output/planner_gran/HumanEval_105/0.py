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
    
    """
    # Step 1: Initialize an empty list to store the filtered numbers
    filtered_nums = []

    # Step 2: Iterate through each number in the input array
    for num in arr:
        # Check if the number is between 1 and 9 (inclusive)
        if 1 <= num <= 9:
            # If the number is within the range, add it to the filtered list
            filtered_nums.append(num)

    # Step 3: Sort the filtered list in ascending order
    filtered_nums.sort()

    # Step 4: Reverse the sorted list to get the desired order
    reversed_nums = filtered_nums[::-1]

    # Step 5: Initialize an empty list to store the final result
    result = []

    # Step 6: Iterate through each number in the reversed list
    for num in reversed_nums:
        # Convert the number to its corresponding name using a mapping
        num_names = {
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
        result.append(num_names[num])

    # Step 7: Return the final result list
    return result