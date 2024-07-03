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
    1. Define a list of vowels (both lowercase and uppercase) for easy comparison.
    2. Initialize a variable to store the closest vowel found so far.
    3. Iterate through the word from right to left using a loop.
    4. Inside the loop:
        a. Check if the current character is a vowel.
        b. If it is, check if the previous character is a consonant.
        c. If both conditions are met, update the closest vowel variable with the current vowel.
        d. If the closest vowel is updated, break the loop as we've found the closest vowel.
    5. After the loop, return the closest vowel found.
    6. If no vowel is found, return an empty string.
    
    Note: Be careful with the iteration direction and the conditions for finding the closest vowel."""
    
    vowels = "aeiouAEIOU"
    closest_vowel = ""
    
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i-1] not in vowels:
                closest_vowel = word[i]
                break
    
    return closest_vowel