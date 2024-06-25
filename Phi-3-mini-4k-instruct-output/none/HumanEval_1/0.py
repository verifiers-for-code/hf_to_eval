
    from typing import List
    import re

    def separate_paren_groups(paren_string: str) -> List[str]:
        # Remove spaces from the input string
        paren_string = paren_string.replace(" ", "")

        # Find all balanced parentheses groups using regex
        paren_groups = re.findall(r'\(([^()]*)\)', paren_string)

        return paren_groups