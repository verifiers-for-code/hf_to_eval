def add(lst):
    """
    Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2

    1. Understand the problem:
       - The function takes a non-empty list of integers as input
       - The goal is to add the even elements that are at odd indices

    2. Process the input list:
       - Iterate through the list using a loop (e.g., for loop)
       - Keep track of the index of each element

    3. Identify even elements at odd indices:
       - Check if the current index is odd (i % 2!= 0)
       - Check if the element at the current index is even (num % 2 == 0)
       - If both conditions are true, consider the element for addition

    4. Calculate the sum of these elements:
       - Initialize a variable to store the sum (total = 0)
       - Add the even element at the odd index to the sum

    5. Return the result:
       - After processing the entire list, return the calculated sum

    Additional implementation details:
    - Use a for loop to iterate through the list with the enumerate function to access both the index and element
    - Use conditional statements (if) to check the conditions for even elements at odd indices
    - Use the modulus operator (%) to check for even and odd numbers
    - Ensure the function handles empty lists and lists with no even elements at odd indices correctly
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 2 != 0 and num % 2 == 0:
            total += num
    return total