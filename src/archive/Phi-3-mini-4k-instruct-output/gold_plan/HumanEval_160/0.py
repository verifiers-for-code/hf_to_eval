def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, 
    and the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Action Plan:
    1. Initialize a string variable 'expression' with the first operand from the 'operand' list.
    2. Use a loop to iterate through the 'operator' list and the remaining elements of the 'operand' list simultaneously:
       - Hint: Consider using the zip() function to pair operators with operands.
    3. In each iteration of the loop:
       - Append the current operator to the 'expression' string.
       - Append the current operand to the 'expression' string.
    4. After the loop, use a built-in Python function to evaluate the 'expression' string as a mathematical expression.
    5. Return the result of the evaluation.

    """
    expression = str(operand[0])
    for op, num in zip(operator, operand[1:]):
        expression += f" {op} {num}"
    return eval(expression)