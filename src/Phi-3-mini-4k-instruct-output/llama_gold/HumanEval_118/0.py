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
    1. Check if the length of the input word is less than 3. If true, return an empty string.
    2. Define a set of vowels (both lowercase and uppercase).
    3. Iterate through the word from right to left (starting from the third character from the end):
       a. Check if the current character is a vowel.
       b. If it's a vowel, check if the preceding and succeeding characters are not vowels.
       c. If the conditions in step 3b are met, return the vowel character.
    4. If no vowel is found between two consonants, return an empty string."""

    # Step 1
    if len(word) < 3:
        return ""

    # Step 2
    vowels = set("aeiouAEIOU")

    # Step 3
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if word[i-1] not in vowels and word[i+1] not in vowels:
                return word[i]

    # Step 4
    return ""