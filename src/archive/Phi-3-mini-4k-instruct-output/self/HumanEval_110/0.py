def is_even(num):
    """Helper function to determine if a number is even."""
    return num % 2 == 0

def exchange(lst1, lst2):
    """Determines if it's possible to exchange elements between lst1 and lst2 to make lst1 a list of only even numbers."""
    even_count_lst1 = sum(is_even(num) for num in lst1)
    even_count_lst2 = sum(is_even(num) for num in lst2)

    # If lst1 is already even or lst2 has more even numbers than lst1, no need to exchange
    if even_count_lst1 == len(lst1) or even_count_lst2 > even_count_lst1:
        return "NO"

    # Attempt exchanges between even numbers in lst1 and lst2
    exchanged_elements = []
    for i in range(len(lst1)):
        if is_even(lst1[i]):
            for j in range(len(lst2)):
                if is_even(lst2[j]) and (lst1[i], lst2[j]) not in exchanged_elements:
                    exchanged_elements.append((lst1[i], lst2[j]))
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    even_count_lst1 += 1
                    even_count_lst2 -= 1
                    if even_count_lst1 == len(lst1):
                        return "YES"
                    break

    return "NO"