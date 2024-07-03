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
    1. Split the word into individual characters and identify consonants and vowels:
        a. Create a list of vowels: "a", "e", "i", "o", "u"
        b. Iterate through the characters in reverse order (starting from the end of the word)
    
    2. Identify the first and last vowels found and mark them:
        a. Use flags to denote the start and end of a vowel sequence
        b. Avoid including first and last vowels in consideration as per the requirements
    
    3. Find and return the first vowel encountered between the first and last marked vowels (if any):
        a. Track vowels found between start and end markers
        b. Return the first vowel in this sequence, or an empty string if none exist
    
    4. Edge cases:
        a. Words without the required conditions: "ab", "FULL" with no vowels between consonants
        b. Words with only one or no vowels: Return an empty string
    
    5. Optimization:
        a. Minimize iterations by skipping already identified vowels and consonants
    
    6. Testing:
        a. Verify with the given examples and additional test cases"""

    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    word_length = len(word)
    start_vowel_index = -1
    end_vowel_index = -1
    found_vowel = False

    # Iterate through the word in reverse order
    for i in range(word_length - 1, -1, -1):
        if word[i] in vowels:
            if not found_vowel:
                start_vowel_index = i
                found_vowel = True
            end_vowel_index = i
        elif found_vowel and word[i] in consonants:
            # Found a consonant after a vowel, so we can return the vowel
            return word[start_vowel_index + 1:end_vowel_index]

    # If no vowel was found between consonants, return an empty string
    return ""