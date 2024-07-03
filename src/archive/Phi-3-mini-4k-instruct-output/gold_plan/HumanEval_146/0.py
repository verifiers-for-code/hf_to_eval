def specialFilter(nums):
    # Step 1: Initialize a counter variable to keep track of numbers meeting the criteria.
    count = 0

    # Step 2: Iterate through each number in the input array 'nums'.
    for num in nums:
        # Step 3: Check if the number is greater than 10.
        if num > 10:
            # Step 4: Convert the number to a string and check if the first and last digits are odd.
            num_str = str(num)
            if int(num_str[0]) % 2 == 1 and int(num_str[-1]) % 2 == 1:
                # If both first and last digits are odd, increment the counter.
                count += 1

    # Step 5: Return the final count.
    return count