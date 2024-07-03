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
    1. Create a dictionary mapping numbers 1-9 to their string representations.
    2. Filter the input array to keep only numbers between 1 and 9 inclusive.
    3. Sort the filtered array in ascending order.
    4. Reverse the sorted array.
    5. Create a new array by mapping each number to its string representation using the dictionary.
    6. Return the resulting array of string representations.

    Note: Implement error handling to manage cases where the input array is empty or contains invalid numbers.
    """
    # Step 1: Create a dictionary mapping numbers 1-9 to their string representations.
    number_to_name = {
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

    # Step 2: Filter the input array to keep only numbers between 1 and 9 inclusive.
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # Step 3: Sort the filtered array in ascending order.
    sorted_arr = sorted(filtered_arr)

    # Step 4: Reverse the sorted array.
    reversed_arr = sorted_arr[::-1]

    # Step 5: Create a new array by mapping each number to its string representation using the dictionary.
    result = [number_to_name[num] for num in reversed_arr]

    # Step 6: Return the resulting array of string representations.
    return result