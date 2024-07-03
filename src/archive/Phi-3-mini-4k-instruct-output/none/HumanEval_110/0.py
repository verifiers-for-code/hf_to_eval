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
    """
    # Count the number of even and odd elements in lst1
    even_count = sum(1 for num in lst1 if num % 2 == 0)
    odd_count = len(lst1) - even_count

    # If all elements in lst1 are even, return "YES"
    if even_count == len(lst1):
        return "YES"

    # If lst1 has no odd elements, we can exchange any odd element from lst2
    if odd_count == 0:
        return "YES"

    # If lst1 has odd elements and lst2 has even elements, we can exchange
    # odd elements from lst1 with even elements from lst2
    if even_count > 0 and odd_count > 0:
        return "YES"

    # If lst1 has odd elements and lst2 has odd elements, it's not possible
    # to make all elements in lst1 even
    return "NO"