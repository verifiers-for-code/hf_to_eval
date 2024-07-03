def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """

    # Step 1: Check if both inputs are of the same type
    if type(a) != type(b):
        # Step 2: Compare their type precedence
        if isinstance(a, str) or isinstance(b, str):
            # Step 3: Handle string cases
            a_clean = a.replace(',', '.')
            b_clean = b.replace(',', '.')
            if float(a_clean) > float(b_clean):
                return b_clean
            elif float(a_clean) < float(b_clean):
                return a_clean
            else:
                return None
        else:
            # Step 4: Edge cases for integers and floats
            if isinstance(a, int) and isinstance(b, float):
                return b
            elif isinstance(a, float) and isinstance(b, int):
                return a
            else:
                # Step 5: Compare integers and floats
                return a if a > b else b
    else:
        # Step 6: If inputs are of the same type, compare them
        if isinstance(a, str):
            a = a.replace(',', '.')
        if isinstance(b, str):
            b = b.replace(',', '.')
        if float(a) > float(b):
            return b
        elif float(a) < float(b):
            return a
        else:
            return None