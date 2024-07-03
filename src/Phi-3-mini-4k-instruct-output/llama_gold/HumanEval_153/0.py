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
    1. Initialize the strongest extension as the first element in the extensions list.
    2. Calculate the strength of the initial strongest extension by counting the number of uppercase letters minus the number of lowercase letters.
    3. Iterate through the remaining extensions in the list:
       a. Calculate the strength of the current extension using the same formula.
       b. If the strength of the current extension is greater than the current strongest extension, update the strongest extension and its strength.
    4. Construct the result string by concatenating the class name, a dot, and the strongest extension name.
    5. Return the result string."""

    # Step 1: Initialize the strongest extension as the first element in the extensions list
    strongest_extension = extensions[0]
    # Step 2: Calculate the strength of the initial strongest extension
    strength = sum(1 for c in strongest_extension if c.isupper()) - sum(1 for c in strongest_extension if c.islower())

    # Step 3: Iterate through the remaining extensions in the list
    for extension in extensions[1:]:
        # Calculate the strength of the current extension
        current_strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        # If the strength of the current extension is greater than the current strongest extension, update the strongest extension and its strength
        if current_strength > strength:
            strongest_extension = extension
            strength = current_strength

    # Step 4: Construct the result string
    result = f"{class_name}.{strongest_extension}"

    # Step 5: Return the result string
    return result