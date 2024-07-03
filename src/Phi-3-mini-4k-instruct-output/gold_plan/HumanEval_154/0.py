def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    Action Plan:
    1. Store the length of the second word (b) in a variable.
    2. Create a pattern string that contains all possible rotations of b:
       - Concatenate b with itself (b + b).
    3. Iterate through the first word (a):
       - For each position in 'a', consider a substring of length equal to b.
    4. For each substring in 'a':
       - Check if it matches any rotation of b in the pattern string:
         - Iterate through the pattern string, checking substrings of length equal to b.
         - If a match is found, return True.
    5. If no match is found after checking all substrings, return False.

    Note: Be careful with the range of iterations to avoid index out of bounds errors.
    """
    b_len = len(b)
    pattern = b + b
    for i in range(len(a) - b_len + 1):
        if a[i:i+b_len] in pattern:
            return True
    return False