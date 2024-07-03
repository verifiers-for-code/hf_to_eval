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
    1. Handle an empty dictionary by returning False
    2. Initialize a variable `all_cases` to track the case of keys. Set it to True initially:
        a. Assume all keys are of the same case for now
    3. Iterate over each item in the dictionary using `dict.items()`:
        a. For each item, check the type of the key
    4. Determine the case of the key:
        a. If the key is a string, check if it's all lowercase or all uppercase
        b. Keep track of the case status across all keys
    5. Handle different key types:
        a. If a non-string key is found, return False early
        b. This step acknowledges the problem's specification requiring all keys to be strings
    6. Compare key cases:
        a. If different cases are found, update `all_cases` to False
    7. At the end of iteration:
        a. If all keys are of the same case, return True
        b. Otherwise, return False
    """
    if not dict:
        return False
    
    all_cases = True
    first_case = None
    
    for key, value in dict.items():
        if not isinstance(key, str):
            return False
        
        if first_case is None:
            first_case = key.islower()
        elif key.islower() != first_case:
            all_cases = False
            break
    
    return all_cases