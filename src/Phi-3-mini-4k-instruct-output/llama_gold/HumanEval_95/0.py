def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    

    Action Plan:
    1. Check if the input dictionary is empty. If so, return False.
    2. Initialize a state variable to track the case of the keys (e.g., "start", "upper", "lower", or "mixed").
    3. Iterate through the keys of the dictionary:
       a. Check if the key is a string. If not, set the state to "mixed" and break the loop.
       b. If the state is "start", determine the case of the key (upper or lower) and set the state accordingly.
       c. If the state is not "start", check if the key's case matches the current state. If not, set the state to "mixed" and break the loop.
    4. After iterating through all keys, return True if the state is "upper" or "lower", and False otherwise.
    """
    if not dict:
        return False
    
    state = "start"
    
    for key in dict.keys():
        if not isinstance(key, str):
            state = "mixed"
            break
        elif state == "start":
            if key.isupper():
                state = "upper"
            elif key.islower():
                state = "lower"
            else:
                state = "mixed"
                break
        elif state != "start":
            if (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                state = "mixed"
                break
    
    return state in ["upper", "lower"]