
    def solve(s):
        result = ""
        for char in s:
            if char.isalpha():
                if char.islower():
                    result += char.upper()
                else:
                    result += char.lower()
            else:
                result += char
        return result