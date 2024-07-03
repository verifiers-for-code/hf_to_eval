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
    1. Initialize counters for odd numbers in lst1 and even numbers in lst2.
    2. Iterate through each element in lst1:
       a. Check if the element is odd (i.e., the remainder of the element divided by 2 is 1).
       b. If the element is odd, increment the odd counter.
    3. Iterate through each element in lst2:
       a. Check if the element is even (i.e., the remainder of the element divided by 2 is 0).
       b. If the element is even, increment the even counter.
    4. Compare the odd counter and even counter:
       a. If the even counter is greater than or equal to the odd counter, return "YES".
       b. Otherwise, return "NO"."""
    
    odd_counter = 0
    even_counter = 0
    
    for num in lst1:
        if num % 2 == 1:
            odd_counter += 1
    
    for num in lst2:
        if num % 2 == 0:
            even_counter += 1
    
    if even_counter >= odd_counter:
        return "YES"
    else:
        return "NO"