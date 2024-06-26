def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Step 1: Create temporary variables to store the original inputs
    temp_a = a
    temp_b = b

    # Step 2: Convert string inputs
    if isinstance(temp_a, str):
        temp_a = temp_a.replace(',', '.')
    if isinstance(temp_b, str):
        temp_b = temp_b.replace(',', '.')

    # Step 3: Convert all inputs to float for comparison
    a = float(temp_a)
    b = float(temp_b)

    # Step 4: Compare the float values
    if a == b:
        return None

    # Step 5: Determine the larger value
    if a > b:
        return temp_a
    else:
        return temp_b