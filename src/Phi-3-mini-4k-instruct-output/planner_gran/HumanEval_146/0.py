def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    

    1. Initialize a counter variable to 0
       - This variable will store the count of numbers that meet the conditions
    
    2. Iterate through each number in the input array:
       a. Check if the current number is greater than 10
       b. If true, proceed to the next step
       c. If false, skip to the next iteration
    
    3. For the number that is greater than 10:
       a. Extract the first digit of the number
          - Convert the number to a string
          - Extract the first character (first digit)
          - Convert it back to an integer
       b. Extract the last digit of the number
          - Convert the number to a string
          - Extract the last character (last digit)
          - Convert it back to an integer
       c. Check if both the first and last digits are odd
          - Use the modulus operator (%) to check if the first digit is odd
          - Use the modulus operator (%) to check if the last digit is odd
       d. If both conditions are met:
          - Increment the counter variable
    
    4. After iterating through all numbers:
       - Return the final count of numbers that meet the conditions
    
    Additional implementation details:
    - Use a for loop to iterate through the input array
    - Use if-else statements to check the conditions and increment the counter
    - Ensure that the function handles empty input arrays correctly
    - Consider adding error handling for non-numeric input values"""
    count = 0
    for num in nums:
        if num > 10:
            first_digit = int(str(num)[0])
            last_digit = int(str(num)[-1])
            if first_digit % 2 == 1 and last_digit % 2 == 1:
                count += 1
    return count