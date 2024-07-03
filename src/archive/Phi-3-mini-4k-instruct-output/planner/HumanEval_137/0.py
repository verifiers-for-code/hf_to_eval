def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    Parameters:
    a (int, float, str): First variable to compare
    b (int, float, str): Second variable to compare

    Returns:
    int, float, str, or None: The larger variable in its given type or None if equal
    """
    # Initialize a variable to store the larger value, initially set to None
    larger_value = None

    # Check the type of a and b
    if type(a) == type(b):
        # If both are integers
        if type(a) is int:
            if a > b:
                larger_value = a
            elif a < b:
                larger_value = b
        # If both are floats
        elif type(a) is float:
            if a > b:
                larger_value = a
            elif a < b:
                larger_value = b
        # If both are strings
        elif type(a) is str:
            # Convert strings to floats for comparison
            a_float = float(a.replace(",", "."))
            b_float = float(b.replace(",", "."))
            if a_float > b_float:
                larger_value = a
            elif a_float < b_float:
                larger_value = b
    else:
        # If the types are different, return None
        return None

    # Return the larger value or None if equal
    return larger_value