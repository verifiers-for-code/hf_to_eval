def digitSum(s):
    """
    This function takes a string as input and returns the sum of the ASCII codes of the uppercase characters only.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of the uppercase characters in the input string.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)
    return sum