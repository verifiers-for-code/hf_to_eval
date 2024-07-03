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
    

    1. Define the vowels and consonants:
       - Create two strings: one for vowels (both lowercase and uppercase) and one for consonants
       - Use these strings for efficient lookup during iteration
    
    2. Initialize variables:
       - Create a variable to store the closest vowel found (initially an empty string)
       - Initialize a flag to indicate if a vowel was found (initially False)
    
    3. Iterate through the word from right to left:
       - Use a loop to iterate through the characters of the word in reverse order
    
    4. Check for consonants and vowels:
       - For each character, check if it's a consonant (not in the consonants string)
       - If it's a consonant, check if the previous character is a vowel (in the vowels string)
       - If a vowel is found, update the closest vowel and set the flag to True
    
    5. Handle edge cases:
       - If the word has only one character, return an empty string
       - If the flag is still False after the iteration, return an empty string
    
    6. Return the closest vowel:
       - If a vowel was found, return the closest vowel
       - Otherwise, return an empty string
    
    Additional implementation details:
    - Use the appropriate string methods for iterating, checking membership, and returning the result
    - Consider using a more efficient data structure (e.g., set) for the vowels and consonants strings
    - Ensure the function handles empty input strings correctly"""

    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    closest_vowel = ""
    found_vowel = False

    if len(word) <= 1:
        return closest_vowel

    for i in range(len(word) - 1, 0, -1):
        if word[i] in consonants:
            if word[i - 1] in vowels:
                closest_vowel = word[i - 1]
                found_vowel = True
                break

    return closest_vowel if found_vowel else ""