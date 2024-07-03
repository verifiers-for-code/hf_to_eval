def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False

    Action Plan:
    1. First, check if the length of the string is less than 3. If so, return False immediately.
    2. If the length is 3 or more, iterate through the string, examining groups of 3 consecutive characters at a time.
       Hint: You'll need to stop the iteration 2 characters before the end of the string.
    3. For each group of 3 characters:
       - Compare the first character with the second and third
       - Compare the second character with the third
       - If any two characters in the group are the same, return False
    4. If you've gone through all groups of 3 without finding any matches, return True
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2]:
            return False

    return True