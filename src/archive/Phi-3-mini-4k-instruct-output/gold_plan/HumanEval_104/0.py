def unique_digits(x):
    # Step 1: Initialize an empty list to store numbers with only odd digits.
    result = []

    # Step 2: Iterate through each number in the input list 'x'.
    for num in x:
        # Step 3a: Convert the number to a string to check individual digits.
        num_str = str(num)

        # Step 3b: Check if all digits in the number are odd.
        if all(int(digit) % 2 != 0 for digit in num_str):
            # If all digits are odd, add the original number to the result list.
            result.append(num)

    # Step 4: Sort the result list in ascending order.
    result.sort()

    # Step 5: Return the sorted list of numbers with only odd digits.
    return result