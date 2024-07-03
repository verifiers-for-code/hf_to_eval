def fix_spaces(text):
    result = ""
    space_counter = 0
    consecutive_spaces = 0

    for char in text:
        if char == " ":
            space_counter += 1
            consecutive_spaces += 1
        else:
            if consecutive_spaces > 2:
                result += "-"
                consecutive_spaces = 0
            elif consecutive_spaces > 0:
                result += "_"
                consecutive_spaces = 0
            result += char
            consecutive_spaces = 0

    # Handle trailing spaces
    if consecutive_spaces > 0:
        if consecutive_spaces > 2:
            result += "-"
        elif consecutive_spaces > 0:
            result += "_"

    return result