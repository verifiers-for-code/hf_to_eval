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
    1. Create an empty list to store the result.
    2. Filter the input array to include only integers between 1 and 9:
        - Use a list comprehension to iterate through the array
        - Check if each element is an integer and within the range 1 to 9
        - Add the filtered elements to a new list
    3. Sort the filtered list in ascending order:
        - Use the built-in `sorted` function
    4. Reverse the sorted list:
        - Use slicing with a step of -1 to reverse the list
    5. Map each digit in the reversed list to its corresponding name:
        - Create a dictionary to map digits to their names (e.g., 1 -> "One", 2 -> "Two", etc.)
        - Use the `map` function to apply the dictionary to the reversed list
        - Convert the resulting map object to a list
    6. Return the final list of names.
    
    Note: Handle edge cases, such as an empty input array, by returning an empty list."""
    
    # Step 1: Create an empty list to store the result
    result = []
    
    # Step 2: Filter the input array to include only integers between 1 and 9
    filtered_arr = [num for num in arr if isinstance(num, int) and 1 <= num <= 9]
    
    # Step 3: Sort the filtered list in ascending order
    sorted_arr = sorted(filtered_arr)
    
    # Step 4: Reverse the sorted list
    reversed_arr = sorted_arr[::-1]
    
    # Step 5: Map each digit in the reversed list to its corresponding name
    digit_to_name = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    result = list(map(digit_to_name.get, reversed_arr))
    
    # Step 6: Return the final list of names
    return result