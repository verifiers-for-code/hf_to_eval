def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator = ['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    # Step 1: Validate input
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list should be equal to the length of operand list minus one.")
    if not all(isinstance(i, int) and i >= 0 for i in operand):
        raise ValueError("Operand list should only contain non-negative integers.")

    # Step 2: Create the expression string
    expression = ""
    for i in range(len(operator)):
        expression += f"{operand[i]}{operator[i]} "
    expression += f"{operand[-1]}"

    # Step 3: Evaluate the expression
    local_vars = {"__builtins__": None}
    local_vars.update({str(i): i for i in operand})
    local_vars.update({"+": lambda x, y: x + y,
                       "-": lambda x, y: x - y,
                       "*": lambda x, y: x * y,
                       "//": lambda x, y: x // y,
                       "**": lambda x, y: x ** y})
    result = eval(expression, local_vars)

    return result