def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14

    Action Plan:
    1. Initialize a list with the first four elements of the sequence: [0, 0, 2, 0]
    2. Check if n is less than 4. If so, return the corresponding element from the initial list
    3. For n >= 4, implement an iterative approach:
       a. Start a loop that runs from 4 to n (inclusive)
       b. In each iteration:
          - Calculate the new element by summing the four elements in the list
          - Append the new element to the end of the list
          - Remove the first (oldest) element from the list
    4. After the loop, return the last element of the list as the result

    This approach ensures efficient computation without recursion and maintains
    only the necessary elements in memory.
    """
    fib4_list = [0, 0, 2, 0]
    if n < 4:
        return fib4_list[n]
    for i in range(4, n + 1):
        new_element = sum(fib4_list)
        fib4_list.append(new_element)
        fib4_list.pop(0)
    return fib4_list[-1]