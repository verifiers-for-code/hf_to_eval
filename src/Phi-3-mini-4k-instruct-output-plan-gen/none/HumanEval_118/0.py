
def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            if i > 0 and word[i-1] in consonants:
                return word[i]
            elif i == 0:
                return word[i]
    return ""