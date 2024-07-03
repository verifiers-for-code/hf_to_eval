def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    

    Action Plan:
    1. Calculate the strength of each extension:
        a. For each extension:
            i. Calculate CAP as the number of uppercase letters
            ii. Calculate SM as the number of lowercase letters
            iii. Determine the extension's strength as CAP - SM
    
    2. Find the strongest extension:
        a. Track the extension with the highest strength
        b. Ensure handling of equal strength by choosing the one that comes first in the list
    
    3. Assemble the output string:
        a. Combine the class name and the strongest extension's name, separated by a dot ('.')
    
    4. Testing:
        a. Validate the function against the provided examples
        b. Consider additional test cases, including edge cases like empty lists and no strongest extension"""

    # Step 1: Calculate the strength of each extension
    strengths = []
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        strengths.append((extension, strength))

    # Step 2: Find the strongest extension
    strongest_extension = max(strengths, key=lambda x: (x[1], -extensions.index(x[0])))

    # Step 3: Assemble the output string
    return f"{class_name}.{strongest_extension[0]}"