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
    # Step 1: Store the original input values in temporary variables to preserve their types
    temp_a = a
    temp_b = b

    # Step 2: If either input is a string, replace any commas with dots (to handle European notation) and convert it to a float for comparison
    if isinstance(temp_a, str):
        temp_a = float(temp_a.replace(',', '.'))
    if isinstance(temp_b, str):
        temp_b = float(temp_b.replace(',', '.'))

    # Step 3: Compare the two values
    if temp_a == temp_b:
        return None
    elif temp_a > temp_b:
        return temp_a
    else:
        return temp_b