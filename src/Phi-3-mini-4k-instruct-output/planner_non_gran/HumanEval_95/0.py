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
    
    2. Check if all keys in the dictionary are strings:
        - Use a conditional statement to check if all keys are strings
        - If not all keys are strings, return False
    
    3. Check if all keys are in lower case or upper case:
        - Iterate through each key in the dictionary
        - For each key, check if it's in lower case or upper case using the `islower()` or `isupper()` methods
        - If any key is not in lower case or upper case, return False
    
    4. If all conditions are met, return True
    
    Note: Use appropriate string methods and conditional statements to implement the logic.
    Be careful to handle the edge case of an empty dictionary correctly.
    """
    if not dict:
        return False
    
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if not (key.islower() or key.isupper()):
            return False
    
    return True