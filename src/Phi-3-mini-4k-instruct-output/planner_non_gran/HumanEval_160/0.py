import operator

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
    1. Understand the problem requirements:
        - The operator list contains basic algebra operations
        - The operand list contains integers
        - The length of the operator list is one less than the length of the operand list
        - The problem requires building and evaluating an algebraic expression
    
    2. Handle the basic algebra operations:
        - Define a dictionary to map operator strings to their corresponding functions
        - Use the operator module to access the required functions (add, sub, mul, truediv, pow)
    
    3. Build the algebraic expression:
        - Initialize an empty string to store the expression
        - Iterate through the operator and operand lists simultaneously
        - For each pair of operator and operand, append the operator and operand to the expression string
    
    4. Evaluate the expression:
        - Use the eval function to evaluate the expression string
        - Be cautious when using eval, as it can execute arbitrary code
    
    5. Return the result:
        - Return the result of the evaluated expression
    
    Note: Be careful when using the eval function, as it can execute arbitrary code. Consider using a safer alternative if necessary.
    """
    # Step 2: Handle the basic algebra operations
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '//': operator.floordiv,
        '**': operator.pow
    }

    # Step 3: Build the algebraic expression
    expression = str(operand[0])
    for op, num in zip(operator, operand[1:]):
        expression += f" {ops[op]} {num}"

    # Step 4: Evaluate the expression
    result = eval(expression)

    # Step 5: Return the result
    return result