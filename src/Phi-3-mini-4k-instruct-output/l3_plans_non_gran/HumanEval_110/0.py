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
    1. Define the function `exchange` with two parameters: `lst1` and `lst2`.
    2. Initialize a variable to store the result (e.g., "YES" or "NO").
    3. Iterate through each element in `lst1`:
        a. Check if the element is odd (not divisible by 2).
        b. If the element is odd, iterate through each element in `lst2`:
            i. Check if the element in `lst2` is even (divisible by 2).
            ii. If the element in `lst2` is even, swap the elements in `lst1` and `lst2`.
            iii. Check if the swapped element in `lst1` is even.
            iv. If the swapped element is even, return "YES" and exit the function.
    4. If no even element is found in `lst2` after iterating through all elements in `lst1`, return "NO".
    5. Consider edge cases, such as empty lists or lists with only one element.
    
    Note: Be careful when swapping elements between the two lists to avoid modifying the original lists."""
    
    result = "NO"
    
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    if lst1[i] % 2 == 0:
                        result = "YES"
                        break
            if result == "YES":
                break
    
    return result