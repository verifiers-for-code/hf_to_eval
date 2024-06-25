def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    """
    # Convert strings to sets to remove duplicates
    set_s0 = set(s0)
    set_s1 = set(s1)

    # Check if both sets have the same length
    if len(set_s0) != len(set_s1):
        return False

    # Check if both sets are equal
    return set_s0 == set_s1