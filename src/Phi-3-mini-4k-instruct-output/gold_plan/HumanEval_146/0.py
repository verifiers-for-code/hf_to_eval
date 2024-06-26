def specialFilter(nums):
    # Initialize a counter variable to keep track of numbers meeting the criteria.
    count = 0

    # Iterate through each number in the input array 'nums'.
    for num in nums:
        # Check if the number is greater than 10.
        if num > 10:
            # Convert the number to a string.
            num_str = str(num)

            # Check if the first character (index 0) of the string is an odd digit.
            if int(num_str[0]) % 2 != 0:
                # Check if the last character (index -1) of the string is an odd digit.
                if int(num_str[-1]) % 2 != 0:
                    # If both first and last digits are odd, increment the counter.
                    count += 1

    # After the iteration, return the final count.
    return count