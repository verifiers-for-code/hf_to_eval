def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    
    :param dict: Input dictionary
    :return: Boolean value indicating if all keys are in lower or upper case
    """
    # Step 1: Check if the input dictionary is empty
    if not dict:
        return False

    # Step 2: Check if all keys in the dictionary are strings
    for key in dict.keys():
        if not isinstance(key, str):
            return False

    # Step 3: Check if all keys are in lower case or upper case
    for key in dict.keys():
        if not (key.islower() or key.isupper()):
            return False

    # Step 4: If all conditions are met, return True
    return True