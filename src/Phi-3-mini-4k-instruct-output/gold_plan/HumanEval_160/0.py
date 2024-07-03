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
    1. Initialize a string variable 'expression' with the first operand from the 'operand' list.
    2. Use a loop to iterate through the 'operator' list and the remaining elements of the 'operand' list simultaneously:
       - Hint: Consider using the zip() function to pair operators with operands.
    3. In each iteration of the loop:
       - Append the current operator to the 'expression' string.
       - Append the current operand to the 'expression' string.
    4. After the loop, use a built-in Python function to evaluate the 'expression' string as a mathematical expression.
    5. Return the result of the evaluation.

    Remember to convert operands to strings when building the expression, and use appropriate 
    string concatenation methods.
    """
    # Step 1: Initialize the expression with the first operand
    expression = str(operand[0])

    # Step 2: Iterate through the operator and operand lists simultaneously
    for op, num in zip(operator, operand[1:]):
        # Step 3: Append the operator and operand to the expression string
        expression += f" {op} {num}"

    # Step 4: Evaluate the expression
    result = eval(expression)

    # Step 5: Return the result
    return result