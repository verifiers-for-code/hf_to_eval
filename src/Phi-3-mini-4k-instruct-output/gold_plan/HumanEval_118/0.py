def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""

    Action Plan:
    1. Check if the word length is less than 3. If so, return an empty string.
    2. Create a set of vowels (both lowercase and uppercase).
    3. Iterate through the word from right to left, starting from the second-to-last character:
       a. Check if the current character is a vowel.
       b. If it is a vowel, check if the characters on both sides are consonants.
       c. If both conditions are met, return the current vowel.
    4. If no vowel is found between consonants, return an empty string.

    Implement the function following this plan to solve the problem.
    """
    if len(word) < 3:
        return ""

    vowels = set("aeiouAEIOU")
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if word[i - 1] not in vowels and word[i + 1] not in vowels:
                return word[i]
    return ""