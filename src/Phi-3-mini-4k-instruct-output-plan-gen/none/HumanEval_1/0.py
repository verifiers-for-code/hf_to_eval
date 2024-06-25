
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Find all balanced parentheses groups using regex
    paren_groups = re.findall(r'\(([^()]*)\)', paren_string)

    return paren_groups

if __name__ == "__main__":
    test_input = '( ) (( )) (( )( ))'
    result = separate_paren_groups(test_input)
    print(result)
```

This script uses regular expressions to find all balanced parentheses groups in the input string. The `re.findall()` function is used with the pattern `'\(([^()]*)\)'`, which matches any substring enclosed in parentheses and captures the content inside. The captured content is then returned as a list of strings.