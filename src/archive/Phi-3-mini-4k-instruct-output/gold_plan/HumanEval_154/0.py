def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    # Step 1: Store the length of the second word (b) in a variable
    b_length = len(b)

    # Step 2: Create a pattern string that contains all possible rotations of b
    pattern = b + b

    # Step 3: Iterate through the first word (a)
    for i in range(len(a) - b_length + 1):
        # Step 4: For each substring in 'a', check if it matches any rotation of b in the pattern string
        substring = a[i:i+b_length]
        for j in range(len(pattern) - b_length + 1):
            if substring == pattern[j:j+b_length]:
                return True

    # Step 5: If no match is found after checking all substrings, return False
    return False