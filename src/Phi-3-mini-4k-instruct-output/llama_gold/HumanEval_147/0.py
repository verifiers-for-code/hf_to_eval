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
    1. Initialize an empty list 'A' to store the values of a[i] = i * i - i + 1 for i from 1 to n.
    2. Use a loop to calculate and store the values in list 'A'.
    3. Initialize an empty list 'ans' to store the valid triples.
    4. Use three nested loops to iterate through the list 'A' with indices i, j, and k, where i < j < k.
    5. Inside the loops, check if the sum of A[i], A[j], and A[k] is a multiple of 3.
    6. If the sum is a multiple of 3, add the triple (A[i], A[j], A[k]) to the 'ans' list.
    7. After the loops, return the length of the 'ans' list, which represents the number of valid triples."""

    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans.append((A[i], A[j], A[k]))

    return len(ans)