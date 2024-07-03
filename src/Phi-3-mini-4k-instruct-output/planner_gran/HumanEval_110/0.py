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
    
    1. Initialize two counters:
       - `count1` to count the number of even numbers in the first list
       - `count2` to count the number of even numbers in the second list
    
    2. Iterate through each element in the first list:
       - Check if the element is even (using the modulus operator `%`)
       - If it's even, increment `count1`
    
    3. Iterate through each element in the second list:
       - Check if the element is even (using the modulus operator `%`)
       - If it's even, increment `count2`
    
    4. Compare the counts:
       - If `count1` is greater than or equal to `count2`, return "YES" (exchange possible)
       - Otherwise, return "NO" (exchange not possible)
    
    Additional implementation details:
    - Use a loop to iterate through each element in the lists
    - Use the modulus operator (`%`) to check if a number is even
    - Ensure the function handles empty input lists correctly
    - Consider adding input validation to check if the input lists are non-empty"""
    
    # Check if input lists are non-empty
    if not lst1 or not lst2:
        return "Invalid input: Lists must be non-empty"
    
    # Initialize counters
    count1 = 0
    count2 = 0
    
    # Count even numbers in lst1
    for num in lst1:
        if num % 2 == 0:
            count1 += 1
    
    # Count even numbers in lst2
    for num in lst2:
        if num % 2 == 0:
            count2 += 1
    
    # Compare counts
    if count1 >= count2:
        return "YES"
    else:
        return "NO"