def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check if both inputs are strings
    if isinstance(a, str) and isinstance(b, str):
        # Remove commas and convert to float
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))

    # Compare the values
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None