def by_length(arr):
    # Helper function to filter, sort, and reverse the list
    def process_numbers(nums):
        # Filter numbers between 1 and 9, sort and reverse
        filtered_sorted_reversed = sorted([num for num in nums if 1 <= num <= 9], reverse=True)
        return filtered_sorted_reversed

    # Helper function to replace numbers with their names
    def replace_with_names(nums):
        # Mapping integers 1-9 to their corresponding names
        num_to_name = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        # Replace each number with its name
        return [num_to_name[num] for num in nums]

    # Main function logic
    if not arr:
        return []

    # Process the input array
    processed_arr = process_numbers(arr)

    # Replace numbers with names
    result = replace_with_names(processed_arr)

    return result