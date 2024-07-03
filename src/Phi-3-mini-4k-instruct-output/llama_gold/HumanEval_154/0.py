def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    

    Action Plan:
    1. Calculate the length of the second word.
    2. Create a pattern by concatenating the second word with itself. This will allow us to check for all possible rotations.
    3. Iterate through the first word, considering substrings of the same length as the second word:
       a. For each substring, iterate through the pattern:
          - Check if the substring matches a part of the pattern.
          - If a match is found, return True immediately.
    4. If no match is found after checking all substrings and rotations, return False."""

    # Step 1: Calculate the length of the second word
    len_b = len(b)

    # Step 2: Create a pattern by concatenating the second word with itself
    pattern = b + b

    # Step 3: Iterate through the first word, considering substrings of the same length as the second word
    for i in range(len(a) - len_b + 1):
        # Extract the substring of the same length as the second word
        substring = a[i:i + len_b]

        # Iterate through the pattern
        for j in range(len(pattern)):
            # Check if the substring matches a part of the pattern
            if substring == pattern[j:j + len_b]:
                # If a match is found, return True immediately
                return True

    # If no match is found after checking all substrings and rotations, return False
    return False