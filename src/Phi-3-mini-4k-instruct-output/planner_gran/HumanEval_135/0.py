def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    

    1. Initialize a variable to store the largest index:
       - Set it to -1, assuming no elements meet the condition
    
    2. Iterate through the array using an index and element:
       - Use a loop that starts from the second element (index 1) to the end of the array
       - For each element, compare it with the previous element
    
    3. Check if the current element meets the condition:
       - If the current element is not greater than or equal to the previous element
       - If the current element is greater than the previous element
    
    4. If the condition is met:
       - Update the largest index variable if the current index is greater than the current largest index
       - Break out of the loop, as we've found the largest index that meets the condition
    
    5. After the loop, return the largest index:
       - If the largest index is still -1, it means no elements met the condition
       - Otherwise, return the largest index
    
    Additional implementation details:
    - Use a for loop to iterate through the array
    - Use an if statement to check the condition for each element
    - Use the break statement to exit the loop when a suitable index is found
    - Ensure that the function handles empty arrays and arrays with a single element correctly"""
    largest_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            largest_index = i
            break
    return largest_index