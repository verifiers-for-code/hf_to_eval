def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Step 1: Check if both inputs are of the same type
    if type(a) == type(b):
        # Step 2: For comparisons involving the same type (integer or float)
        if isinstance(a, (int, float)):
            # Cast both inputs to float for a uniform comparison
            a, b = float(a), float(b)
            # Use built-in comparison operators to determine the larger value
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return None
        # Step 3: Handle string cases
        else:
            # Remove the separator (either ' or ',') from the string representation
            a = a.replace(',', '.')
            b = b.replace(',', '.')
            # Compare the floats for the string representations after the cleanup
            if float(a) > float(b):
                return a
            elif float(a) < float(b):
                return b
            else:
                return None
    else:
        # Step 4: Edge cases
        # Compare the types to determine which one is larger
        if type(a) == int and type(b) == float:
            return b
        elif type(a) == float and type(b) == int:
            return a
        elif type(a) == str and type(b) == int:
            return b
        elif type(a) == int and type(b) == str:
            return a
        else:
            # If none of the above cases match, return None
            return None