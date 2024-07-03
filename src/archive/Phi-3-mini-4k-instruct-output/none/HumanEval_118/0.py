def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    for i in range(len(word)-2, -1, -1):
        if word[i] not in vowels:
            if word[i+1] in vowels:
                return word[i+1]
            else:
                return ""
    return ""