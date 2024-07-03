def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example:
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).

    Action Plan:
    1. Initialize an empty array a of length n.
    2. Iterate through the array a from index 1 to n:
        a. Calculate the value of a[i] using the formula i * i - i + 1.
        a. Store the calculated value in the array a.
    3. Initialize a variable count to 0 to store the number of valid triples.
    4. Iterate through the array a from index 1 to n-2:
        a. For each i, iterate through the array a from index i+1 to n-1:
            - Calculate the sum of a[i], a[j], and a[k].
            - Check if the sum is divisible by 3 (i.e., sum % 3 == 0).
            - If the condition is met, increment the count variable.
    5. Return the count variable, which represents the number of valid triples.
    
    Note: Use a nested loop to iterate through the array a and check for the condition.
    Be careful with the indexing and the modulo operation.
    """
    a = [i * i - i + 1 for i in range(1, n+1)]
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count