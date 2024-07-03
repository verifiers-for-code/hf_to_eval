def digitSum(s):
    """
    Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    

    1. Initialize a variable to store the sum of the ASCII codes
       - Set the initial value to 0
    
    2. Iterate through each character in the input string:
       a. Check if the character is an uppercase letter using a string method
       b. If the character is uppercase:
          - Calculate the ASCII code of the character using a built-in function
          - Add the ASCII code to the sum variable
    
    3. After iterating through all characters, return the sum of the ASCII codes
    
    Implementation details:
    - Use a loop (e.g., for loop) to iterate through the characters in the string
    - Use a string method (e.g., isupper()) to check if a character is uppercase
    - Use a built-in function (e.g., ord()) to get the ASCII code of a character
    - Ensure that the function handles empty input strings correctly (returning 0)
    - Consider using a more concise approach, such as using a generator expression and the sum() function, to calculate the sum of the ASCII codes
    """
    return sum(ord(c) for c in s if c.isupper())