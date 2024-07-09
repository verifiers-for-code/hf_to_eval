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
    1. Define the function do_algebra with two parameters: operator and operand
    2. Initialize an empty string to store the algebraic expression
    3. Iterate through the operator and operand lists:
        a. For each operator, add it to the expression string
        b. For each operand, add it to the expression string
    4. Use the eval() function to evaluate the algebraic expression
    5. Return the result of the evaluation
    6. Consider edge cases:
        a. Check if the operator list has at least one operator and the operand list has at least two operands
        b. Handle potential errors, such as invalid operators or operands
    7. Test the function with example inputs to ensure correct behavior
    """
    # Check if the operator list has at least one operator and the operand list has at least two operands
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Invalid input: operator list must have at least one operator and operand list must have at least two operands")

    # Initialize an empty string to store the algebraic expression
    expression = ""

    # Iterate through the operator and operand lists
    for i in range(len(operator)):
        # Add the operator to the expression string
        expression += str(operator[i])
        # Add the operand to the expression string
        expression += str(operand[i])

    # Use the eval() function to evaluate the algebraic expression
    result = eval(expression)

    # Return the result of the evaluation
    return result