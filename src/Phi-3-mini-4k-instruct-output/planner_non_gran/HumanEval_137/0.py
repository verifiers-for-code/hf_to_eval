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
    

    Action Plan:
    1. Define the function `compare_one` with two parameters `a` and `b`.
    2. Initialize a variable to store the larger value, initially set to `None`.
    3. Check the type of `a` and `b`:
        a. If both are integers, compare their values and update the larger value accordingly.
        b. If both are floats, compare their values and update the larger value accordingly.
        c. If both are strings, compare their values as floats (considering possible decimal separators) and update the larger value accordingly.
        d. If the types are different, return `None` as the values cannot be compared.
    4. After the type checks, return the larger value or `None` if the values are equal.
    5. Consider the representation of real numbers as strings:
        a. When comparing strings, use the `float()` function to convert them to floats for comparison.
        b. Be aware of potential issues with decimal separators (e.g., `.` or `,`) in string representations.
    """
    if type(a) == type(b):
        if type(a) in [int, float]:
            return a if a > b else b
        elif type(a) == str:
            a_val = float(a.replace(',', '.'))
            b_val = float(b.replace(',', '.'))
            return a if a_val > b_val else b
    return None