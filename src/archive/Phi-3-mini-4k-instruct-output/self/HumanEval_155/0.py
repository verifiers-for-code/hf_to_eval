def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)

    Action Plan:
    1. Transform the number to a positive integer:
        - Use the `abs()` function to ensure that negative signs are not considered during digit evaluation
    2. Convert the absolute value to a string:
        - This allows us to iterate over each digit
    3. Iterate through each character in the string:
        - Convert each character back to an integer for evaluation
    4. Initialize variables to count even and odd digits:
        - Initialize even_count and odd_count to zero
    5. Evaluate and increment the appropriate count:
        - For each digit, check if it's divisible by 2 (even) or not (odd)
        - Update even_count or odd_count accordingly
    6. Return a tuple with the counts of even and odd digits:
        - Return (even_count, odd_count)"""

    # Step 1: Transform the number to a positive integer
    num = abs(num)

    # Step 2: Convert the absolute value to a string
    num_str = str(num)

    # Step 3: Iterate through each character in the string
    even_count = 0
    odd_count = 0
    for digit in num_str:
        # Step 4: Initialize variables to count even and odd digits

        # Step 5: Evaluate and increment the appropriate count
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Step 6: Return a tuple with the counts of even and odd digits
    return (even_count, odd_count)