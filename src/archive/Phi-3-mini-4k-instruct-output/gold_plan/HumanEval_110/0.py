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
    1. Initialize two counters: one for odd numbers in lst1 and one for even numbers in lst2
    2. Iterate through lst1:
       - For each number, check if it's odd (hint: use modulo operator)
       - If odd, increment the odd counter
    3. Iterate through lst2:
       - For each number, check if it's even
       - If even, increment the even counter
    4. Compare the counters:
       - If there are enough or more even numbers in lst2 than odd numbers in lst1, return "YES"
       - Otherwise, return "NO"
    5. Ensure the function returns the correct string value ("YES" or "NO")
    """
    odd_count = 0
    even_count = 0

    for num in lst1:
        if num % 2 != 0:
            odd_count += 1

    for num in lst2:
        if num % 2 == 0:
            even_count += 1

    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"