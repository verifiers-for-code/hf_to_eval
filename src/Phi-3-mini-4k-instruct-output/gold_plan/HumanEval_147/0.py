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
    1. Generate the array 'a':
       - Create a list comprehension that calculates a[i] for i from 1 to n
       - Use the formula: i * i - i + 1

    2. Initialize a counter for valid triples

    3. Implement three nested loops to iterate through all possible triples:
       - Outer loop: i from 0 to n-3
       - Middle loop: j from i+1 to n-2
       - Inner loop: k from j+1 to n-1

    4. Inside the innermost loop:
       - Calculate the sum of a[i], a[j], and a[k]
       - Check if the sum is divisible by 3 (use the modulo operator)
       - If divisible by 3, increment the counter

    5. Return the final count of valid triples
    """
    a = [i * i - i + 1 for i in range(1, n+1)]
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count