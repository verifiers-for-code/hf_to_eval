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
    1. Create an integer array a of length n:
       - Initialize an empty list or array to store the values of a[i]
       - Use a loop or list comprehension to calculate the values of a[i] = i * i - i + 1 for each i from 1 to n
    
    2. Initialize a counter variable to store the number of triples:
       - Initialize a variable (e.g., count) to 0
    
    3. Iterate over all possible combinations of three indices i, j, and k:
       - Use three nested loops to iterate over the indices i, j, and k
       - Ensure that i < j < k for each combination
    
    4. Check if the sum of a[i], a[j], and a[k] is a multiple of 3:
       - Calculate the sum a[i] + a[j] + a[k]
       - Check if the sum is divisible by 3 (i.e., the remainder is 0)
    
    5. If the sum is a multiple of 3, increment the counter:
       - Increment the count variable by 1
    
    6. Return the final count:
       - After iterating over all possible combinations, return the count variable
    
    Additional implementation details:
    - Use appropriate data structures and methods for creating the array and iterating over the indices
    - Ensure that the function handles edge cases, such as n = 0 or n = 1
    - Consider optimizing the implementation to reduce the time complexity, if possible
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count