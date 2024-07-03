def sum_of_digits(N):
    """Helper function to sum digits of a number."""
    return sum(int(digit) for digit in str(N))

def N_to_binary(N):
    """Helper function to convert an integer to its binary representation."""
    return bin(N)[2:]

def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary."""
    # Step 1: Initialize variables
    sum_of_digits = 0

    # Step 2: Validate input
    if not isinstance(N, int) or N < 0 or N > 10000:
        return "Invalid input. Please enter a positive integer between 0 and 10000."

    # Step 3: Main function implementation
    binary_representation = N_to_binary(N)
    sum_of_digits = sum_of_digits(binary_representation)

    # Step 5: Manage edge cases
    if not binary_representation:
        return "Invalid input. The binary representation is empty."

    # Step 6: Optimization suggestions
    # The provided solution is already optimized for the problem.

    # Step 7: Testing strategy
    # Test with provided examples
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"

    # Test with other edge cases
    assert solve(0) == "0"
    assert solve(10000) == "1001110000000"

    # Test with invalid inputs
    assert solve(-1) == "Invalid input. Please enter a positive integer between 0 and 10000."
    assert solve(10001) == "Invalid input. Please enter a positive integer between 0 and 10000."

    # Test with non-integer inputs
    assert solve("1000") == "Invalid input. Please enter a positive integer between 0 and 10000."

    print("All tests passed!")

    return bin(sum_of_digits)[2:]