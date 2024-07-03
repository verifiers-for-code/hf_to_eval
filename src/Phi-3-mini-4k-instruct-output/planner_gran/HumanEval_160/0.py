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

    1. Check the input lists and their lengths:
       - Verify that the length of the operator list is equal to the length of the operand list minus one
       - Ensure that both lists have at least one element
    
    2. Initialize an empty expression string:
       - This string will be used to build the algebraic expression
    
    3. Iterate through the operator and operand lists:
       - Use a loop to iterate through the lists, considering each operator and operand pair
       - For each iteration:
         a. Append the current operator and operand to the expression string
         b. If the operator is '+' or '-', append the operand to the expression string
         c. If the operator is '*' or '//', append the operand to the expression string
         d. If the operator is '**', append the operand to the expression string
    
    4. Evaluate the algebraic expression:
       - Use the eval() function to evaluate the expression string
       - This will perform the arithmetic operations and return the result
    
    5. Return the evaluation result:
       - The function should return the final result of the evaluated expression
    
    Additional implementation details:
    - Use the correct syntax for building the expression string (e.g., '2 + 3' instead of '2 + 3 =')
    - Handle operator precedence and order of operations correctly
    - Consider using a more robust method for evaluating the expression, such as using a stack or implementing a simple expression parser
    - Ensure that the function handles invalid input (e.g., empty lists, invalid operators) correctly"""

    # Check the input lists and their lengths
    if len(operator) != len(operand) - 1 or len(operator) == 0 or len(operand) == 0:
        return "Invalid input"

    # Initialize an empty expression string
    expression = ""

    # Iterate through the operator and operand lists
    for i in range(len(operator)):
        # Append the current operator and operand to the expression string
        expression += str(operand[i])

        # If the operator is '+' or '-', append the operand to the expression string
        if operator[i] == '+':
            expression += " + "
        elif operator[i] == '-':
            expression += " - "

        # If the operator is '*' or '//', append the operand to the expression string
        elif operator[i] == '*':
            expression += " * "
        elif operator[i] == '//':
            expression += " // "

        # If the operator is '**', append the operand to the expression string
        elif operator[i] == '**':
            expression += " ** "

    # Evaluate the algebraic expression
    result = eval(expression)

    # Return the evaluation result
    return result