def by_length(arr):
    # Step 1: Create a dictionary mapping numbers 1-9 to their string representations.
    num_to_str = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }

    # Step 2: Filter the input array to keep only numbers between 1 and 9 inclusive.
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # Step 3: Sort the filtered array in ascending order.
    sorted_arr = sorted(filtered_arr)

    # Step 4: Reverse the sorted array.
    reversed_arr = sorted_arr[::-1]

    # Step 5: Create a new array by mapping each number to its string representation using the dictionary.
    result = [num_to_str[num] for num in reversed_arr]

    # Step 6: Return the resulting array of string representations.
    return result