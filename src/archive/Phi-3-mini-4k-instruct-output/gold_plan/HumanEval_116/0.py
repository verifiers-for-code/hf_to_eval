def count_ones_in_binary(num):
    """
    Helper function to count the number of '1's in the binary representation of a number.
    """
    binary_representation = bin(num)[2:]
    return binary_representation.count('1')

def sort_array(arr):
    """
    Sorts an array of non-negative integers according to the number of ones in their binary representation in ascending order.
    For similar number of ones, sorts based on decimal value.
    """
    # Step 1: Sort the array based on decimal values
    arr = sorted(arr)

    # Step 2: Sort the array based on the count of '1's in binary representation
    arr = sorted(arr, key=count_ones_in_binary)

    return arr