
def maximum(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)

    # Return the first k elements
    return arr[:k]