def get_collatz(n):
    """
    Generate the Collatz sequence for a given number.
    """
    if n == 1:
        return [1]
    elif n < 1:
        raise ValueError("Input must be a positive integer.")
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in Collatz sequence.
    """
    collatz_sequence = get_collatz(n)
    odd_numbers = [num for num in collatz_sequence if num % 2 != 0]
    odd_numbers.sort()
    return odd_numbers