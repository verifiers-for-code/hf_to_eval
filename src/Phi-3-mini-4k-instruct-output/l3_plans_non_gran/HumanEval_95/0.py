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
    1. Check if the input dictionary is empty:
        - If empty, return False immediately
    
    2. Initialize a flag variable to True, assuming all keys are in the desired case
    
    3. Iterate through each key in the dictionary:
        - For each key, check its case:
            a. If the key is in lower case, set the flag variable to False
            b. If the key is in upper case, set the flag variable to False
            c. If the key is neither in lower nor upper case, set the flag variable to False
    
    4. After iterating through all keys, return the flag variable:
        - If the flag is still True, all keys are in the desired case (lower or upper)
        - If the flag is False, not all keys are in the desired case
    
    Note: Use appropriate string methods for case checking (e.g., `islower()`, `isupper()`).
    Be careful to handle the edge case of an empty dictionary correctly.
    """
    if not dict:
        return False
    
    flag = True
    for key in dict.keys():
        if not (key.islower() or key.isupper()):
            flag = False
            break
    
    return flag