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
    

    Action Plan:
    1. Initialize a variable (e.g., `sum`) to store the sum of upper character ASCII codes, set it to 0.
    2. Iterate through each character in the input string:
        a. Check if the character is an uppercase letter using the `isupper()` method.
        b. If the character is uppercase:
            - Convert the character to its ASCII code using the `ord()` function.
            - Add the ASCII code to the `sum` variable.
    3. After iterating through all characters, return the final `sum` value.
    """
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)
    return sum