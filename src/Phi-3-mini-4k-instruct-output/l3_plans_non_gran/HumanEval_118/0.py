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
    1. Define a list of vowels (both lowercase and uppercase) to check against.
    2. Initialize a variable to store the closest vowel found.
    3. Iterate through the word from right to left (using reversed iteration):
        a. For each character in the word:
            - Check if the character is a vowel (case-insensitive).
            - If it's a vowel, check if the previous character is a consonant (case-insensitive).
            - If both conditions are met, update the closest vowel variable with the current vowel.
    4. After iterating through the entire word, return the closest vowel found.
        - If no vowel meets the condition, return an empty string."""
    
    vowels = "aeiouAEIOU"
    closest_vowel = ""
    
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i-1] not in vowels:
                closest_vowel = word[i]
                break
    
    return closest_vowel