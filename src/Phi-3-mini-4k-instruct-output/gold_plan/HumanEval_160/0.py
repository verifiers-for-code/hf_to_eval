def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, 
    and the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.

    Args:
    operator (list): A list of basic algebra operations.
    operand (list): A list of non-negative integers.

    Returns:
    int: The result of the algebraic expression.
    """
    # Initialize a string variable 'expression' with the first operand from the 'operand' list.
    expression = str(operand[0])

    # Use a loop to iterate through the 'operator' list and the remaining elements of the 'operand' list simultaneously.
    for op, num in zip(operator, operand[1:]):
        # Append the current operator to the 'expression' string.
        expression += f" {op} "
        # Append the current operand to the 'expression' string.
        expression += str(num)

    # Evaluate the 'expression' string as a mathematical expression.
    result = eval(expression)

    return result