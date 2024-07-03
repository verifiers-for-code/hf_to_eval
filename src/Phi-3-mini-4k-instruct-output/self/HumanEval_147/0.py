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
    1. Generate array `a`:
        a. Create an empty list, `a`
        b. Use a loop to populate `a` with the values given by the formula a[i] = i*i - i + 1 for i in range(1, n+1)
    
    2. Count triples meeting the criteria:
        a. Initialize a counter to keep track of valid triples
        b. Use three nested loops to generate all possible triples (i, j, k) where i < j < k
        c. In each iteration of the innermost loop, check if a[i] + a[j] + a[k] is divisible by 3
        d. If the condition is met, increment the counter
    
    3. Edge cases and optimization:
        a. For large n, consider using combinatorial libraries or methods to reduce iterations
        b. Ensure loops iterate over all valid indices without unnecessary checks (e.g., when k > n or i + j > k)
    
    4. Return the final count of valid triples
    
    5. Validate the function with given test cases and additional edge cases (like small values of n or n with large array contents)"""
    
    a = [i*i - i + 1 for i in range(1, n+1)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count