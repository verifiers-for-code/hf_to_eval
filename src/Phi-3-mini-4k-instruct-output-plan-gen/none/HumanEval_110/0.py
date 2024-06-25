
def exchange(lst1, lst2):
    # Count the number of even and odd elements in lst1
    even_count = sum(1 for num in lst1 if num % 2 == 0)
    odd_count = len(lst1) - even_count

    # If all elements in lst1 are even, return "YES"
    if even_count == len(lst1):
        return "YES"

    # If lst1 has no odd elements, we can exchange odd elements from lst2
    if odd_count == 0:
        return "YES"

    # If lst1 has odd elements and lst2 has even elements, we can exchange elements
    if even_count > 0 and odd_count > 0:
        return "YES"

    # If lst1 has odd elements and lst2 has no even elements, it's not possible to make lst1 even
    return "NO"