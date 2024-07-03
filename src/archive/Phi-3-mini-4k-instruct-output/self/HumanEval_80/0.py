def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Action Plan:
    1. Validate input:
        - Check if the length of the input string is less than 3
        - If so, return False immediately
    2. Use a loop to iterate through the string, with a sliding window of 3 letters:
        a. Ensure you start from index 0 to the second-last index to avoid going out of bounds
    3. Inside the loop, create a sub-string of 3 consecutive letters:
        a. Extract the current 3-letter substring
    4. Compare the current substring with previous substrings:
        a. Check if any substring in the previously checked set has an identical set of 3 letters
        b. If so, return False
    5. Keep track of checked substrings using a set data structure.
    6. After the loop completes (no duplicates found), check if the length of the string is at least 3:
        a. Return True if so, else return False
    """
    if len(s) < 3:
        return False

    checked_substrings = set()

    for i in range(len(s) - 2):
        substring = s[i:i+3]
        if substring in checked_substrings:
            return False
        checked_substrings.add(substring)

    return len(s) >= 3