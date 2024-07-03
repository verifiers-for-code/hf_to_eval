def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    

    Action Plan:
    1. Create a helper function to generate the Collatz sequence for a given number:
        - Handle the base case for n = 1
        - Use a loop or recursion to compute each subsequent number following Collatz rules
    
    2. Generate the Collatz sequence for the input number:
        - Use the helper function on n
    
    3. Filter the sequence to keep only the odd numbers:
        - Use list comprehension with an appropriate condition to filter odd numbers
    
    4. Sort the resulting filtered list:
        - Use the sort() method or sorted() function
    
    5. Edge cases to consider:
        - The input number is 1 (return only 1 as a list)
        - The input number is less than 1 (handle error or return an empty list)
    
    6. Optimize for efficiency:
        - Minimize repeated computations, especially within the loop
        - Recurse effectively, considering memoization for larger inputs
    
    7. Ensure correctness by testing the function with the provided examples and additional test cases.
    """
    if n < 1:
        return []

    def collatz_sequence(n):
        if n == 1:
            return [1]
        elif n % 2 == 0:
            return [n] + collatz_sequence(n // 2)
        else:
            return [n] + collatz_sequence(3 * n + 1)

    sequence = collatz_sequence(n)
    odd_numbers = [num for num in sequence if num % 2 != 0]
    odd_numbers.sort()
    return odd_numbers