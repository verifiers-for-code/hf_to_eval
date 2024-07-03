def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    

    Action Plan:
    1. Understand the problem:
        - Two lists of numbers are given: lst1 and lst2
        - The goal is to determine if it's possible to exchange elements between lst1 and lst2 to make all elements in lst1 even
        - There's no limit on the number of exchanges
    
    2. Identify the conditions for a successful exchange:
        - All elements in lst1 must be even
        - There must be at least one even element in lst2
    
    3. Implement the logic to check for the conditions:
        - Check if all elements in lst1 are even using a loop or a built-in function
        - Check if there's at least one even element in lst2 using a loop or a built-in function
    
    4. Return the appropriate result:
        - If both conditions are met, return "YES"
        - If either condition is not met, return "NO"
    
    Note: Consider using list comprehensions or built-in functions to simplify the implementation.
    Be careful to handle edge cases, such as empty lists or lists with no even elements."""
    
    # Check if all elements in lst1 are even
    if all(x % 2 == 0 for x in lst1):
        # Check if there's at least one even element in lst2
        if any(x % 2 == 0 for x in lst2):
            return "YES"
    return "NO"