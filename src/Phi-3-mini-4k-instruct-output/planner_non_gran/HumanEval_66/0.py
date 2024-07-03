def digitSum(s):
    """
    Task:
    Write a function that takes a string as input and returns the sum of the upper characters only's ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153

    Action Plan:
    1. Define a function `digitSum` that takes a string `s` as input.
    2. Initialize a variable `sum` to 0, which will store the sum of ASCII codes.
    3. Iterate through each character `char` in the input string `s`:
        a. Check if the character `char` is uppercase using the `isupper()` method.
        b. If `char` is uppercase, add its ASCII code to the `sum` using the `ord()` function.
    4. After iterating through all characters, return the final `sum`.
    5. Consider adding a docstring to explain the function's purpose, parameters, and return value.

    Note: Use the `isupper()` method to check if a character is uppercase.
    Use the `ord()` function to get the ASCII code of a character."""
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)
    return sum