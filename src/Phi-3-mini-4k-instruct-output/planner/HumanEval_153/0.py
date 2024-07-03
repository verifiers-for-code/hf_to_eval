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
    1. Initialize an empty list to store the strengths of each extension.
    2. Iterate through the list of extensions:
        a. For each extension, calculate its strength using the formula: CAP - SM, where CAP is the number of uppercase letters and SM is the number of lowercase letters.
        b. Add the calculated strength to the list of strengths.
    3. Find the index of the maximum strength in the list of strengths.
    4. Use the index to retrieve the corresponding extension from the original list.
    5. Return the result in the format: ClassName.StrongestExtensionName, where ClassName is the input class name and StrongestExtensionName is the strongest extension.
    
    Note: Use appropriate string methods to count uppercase and lowercase letters.
    Be careful when handling the case where there are multiple extensions with the same strength."""
    
    strengths = []
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        strengths.append(strength)
    
    max_strength = max(strengths)
    max_strength_index = strengths.index(max_strength)
    strongest_extension = extensions[max_strength_index]
    
    return f"{class_name}.{strongest_extension}"