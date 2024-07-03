def get_closest_vowel(word):
    vowels = "aeiou"
    start_vowel = False
    end_vowel = False
    vowel_sequence = []
    
    # Step 1: Iterate through the characters in reverse order
    for char in reversed(word):
        if char in vowels:
            if not start_vowel:
                start_vowel = True
            if start_vowel and not end_vowel:
                end_vowel = True
            vowel_sequence.append(char)
    
    # Step 2: Handle edge cases
    if len(vowel_sequence) < 2:
        return ""
    
    # Step 3: Find and return the first vowel encountered between the first and last marked vowels
    for vowel in vowel_sequence[1:-1]:
        if vowel in vowels:
            return vowel
    
    return ""