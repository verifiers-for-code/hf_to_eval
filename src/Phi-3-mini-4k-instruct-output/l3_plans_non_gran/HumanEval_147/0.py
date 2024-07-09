def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    

    Action Plan:
    1. Initialize a variable count to store the number of triples.
    2. Create an integer array a of length n, where each element a[i] is calculated as i * i - i + 1.
    3. Iterate over the array a using three nested loops:
        a. The outer loop iterates from i = 0 to n-1.
        b. The middle loop iterates from j = i + 1 to n-1.
        c. The inner loop iterates from k = j + 1 to n-1.
    4. Inside the inner loop, check if the sum of a[i], a[j], and a[k] is a multiple of 3.
    5. If the condition is met, increment the count variable.
    6. After the loops, return the count variable, which represents the number of triples that meet the conditions."""

    count = 0
    a = [i * i - i + 1 for i in range(1, n+1)]

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1

    return count