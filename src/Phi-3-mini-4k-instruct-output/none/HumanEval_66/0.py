def digitSum(s):
    """
    Write a function that takes a string as input and returns the sum of the ASCII codes of the uppercase characters only.
    """
    sum_ascii = 0
    for char in s:
        if char.isupper():
            sum_ascii += ord(char)
    return sum_ascii