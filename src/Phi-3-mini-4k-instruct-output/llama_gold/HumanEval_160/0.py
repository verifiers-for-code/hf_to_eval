def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    

    Action Plan:
    1. Initialize an empty string to build the algebraic expression.
    2. Start the expression with the first operand as a string.
    3. Iterate through the operator list and the remaining operands (from the second operand onwards) simultaneously:
       a. For each iteration, append the current operator and the corresponding operand (as a string) to the expression.
    4. After iterating through all operators and operands, the expression string is complete.
    5. Use the eval function to evaluate the expression string and return the result.
    """
    expression = str(operand[0])
    for op, num in zip(operator, operand[1:]):
        expression += f" {op} {num}"
    return eval(expression)