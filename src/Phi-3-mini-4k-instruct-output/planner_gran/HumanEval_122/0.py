def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    

    1. Initialize a variable to store the sum of the filtered elements
       - Set the initial value to 0
    
    2. Iterate over the first k elements of the input array:
       - Use a loop to process each element in the array
    
    3. For each element, check its length:
       - Use the len() function to get the number of digits in the element
    
    4. If the element has at most two digits:
       - Add the element to the sum variable
    
    5. After processing all k elements, return the sum:
       - The sum variable now holds the sum of the elements with at most two digits
    
    Additional implementation details:
    - Use a for loop to iterate over the first k elements
    - Use the len() function to check the length of each element
    - Use a conditional statement (if) to filter elements with at most two digits
    - Use the += operator to add elements to the sum variable
    - Ensure the function handles edge cases, such as an empty input array or k being larger than the array length"""
    sum_of_elements = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_of_elements += arr[i]
    return sum_of_elements