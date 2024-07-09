def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    Action Plan:
    1. Define the function cycpattern_check with two parameters: a (first word) and b (second word)
    2. Initialize a variable to store the rotated word
    3. Iterate over the length of the second word:
        a. Rotate the second word by one character to the right at each iteration
        b. Store the rotated word in the variable
    4. Check if the rotated word is a substring of the first word using the 'in' operator
    5. Return True if the rotated word is found, False otherwise
    6. Consider using a loop or list comprehension to generate all possible rotations of the second word
    7. Ensure the function is case-sensitive and handles words with different cases
    """
    rotated_word = b
    for i in range(len(b)):
        rotated_word = rotated_word[-1] + rotated_word[:-1]
        if rotated_word in a:
            return True
    return False