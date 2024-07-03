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
    """
    # Check if the input dictionary is empty
    if not dict:
        return False
    
    # Initialize a variable to store the result
    result = True
    
    # Iterate through each key in the dictionary
    for key in dict:
        # Check the case of the current key
        if not (key.islower() or key.isupper()):
            # If the key is not in the desired case, set the result variable to False
            result = False
            # Break out of the loop, as we've found a key that doesn't meet the condition
            break
    
    # Return the result
    return result