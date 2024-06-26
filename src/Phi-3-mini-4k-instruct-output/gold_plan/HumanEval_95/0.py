def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dict:
        return False

    state = "start"

    for key in dict.keys():
        if not isinstance(key, str):
            state = "mixed"
            break

        if state == "start":
            if key.isupper():
                state = "upper"
            elif key.islower():
                state = "lower"
            else:
                break
        else:
            if state == "upper" and not key.isupper():
                state = "mixed"
            elif state == "lower" and not key.islower():
                state = "mixed"
            else:
                break

    return state in ["upper", "lower"]