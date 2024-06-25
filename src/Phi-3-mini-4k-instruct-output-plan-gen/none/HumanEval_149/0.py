
def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered_lst = [word for word in lst if len(word) % 2 == 0]

    # Sort the list by length and alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))

    return sorted_lst