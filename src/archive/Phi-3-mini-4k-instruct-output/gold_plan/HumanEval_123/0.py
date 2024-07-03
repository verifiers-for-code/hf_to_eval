def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.
    """
    # Step 1: Initialize an empty list to store odd numbers in the Collatz sequence.
    odd_numbers = []

    # Step 2: Check if the input n is odd. If so, add it to the list.
    if n % 2 != 0:
        odd_numbers.append(n)

    # Step 3: Implement a loop that continues until n becomes 1
    while n != 1:
        # Step 3a: If n is even, divide it by 2.
        if n % 2 == 0:
            n = n // 2
        # Step 3b: If n is odd, multiply it by 3 and add 1.
        else:
            n = n * 3 + 1
        # Step 3c: If the new n is odd, add it to the list.
        if n % 2 != 0:
            odd_numbers.append(n)

    # Step 4: Ensure that 1 is added to the list if it's not already present.
    if 1 not in odd_numbers:
        odd_numbers.append(1)

    # Step 5: Sort the list in ascending order.
    odd_numbers.sort()

    # Step 6: Return the sorted list of odd numbers.
    return odd_numbers