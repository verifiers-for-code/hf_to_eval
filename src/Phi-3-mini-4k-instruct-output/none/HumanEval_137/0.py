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
    # Check if both inputs are strings
    if isinstance(a, str) and isinstance(b, str):
        # Remove commas from the strings
        a = a.replace(',', '.')
        b = b.replace(',', '.')
        # Compare the floats
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
        else:
            return None
    # Check if both inputs are integers
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    # Check if one input is a string and the other is a number
    elif isinstance(a, str) and isinstance(b, (int, float)):
        a = a.replace(',', '.')
        if float(a) > b:
            return a
        elif float(a) < b:
            return b
        else:
            return None
    elif isinstance(a, (int, float)) and isinstance(b, str):
        b = b.replace(',', '.')
        if a > float(b):
            return a
        elif a < float(b):
            return b
        else:
            return None