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
    1. Initialize variables:
       - Set the first extension as the strongest
       - Calculate its strength (uppercase count - lowercase count)

    2. Create a loop to iterate through all extensions:
       - For each extension, calculate its strength
       - Compare the strength with the current strongest
       - If stronger, update the strongest extension and its strength

    3. After the loop, format the result:
       - Combine the class_name and the strongest extension with a dot

    4. Return the formatted result

    Note: To count uppercase and lowercase letters, consider using list comprehensions
    with conditions checking for alphabetic characters and their case.
    """

    # Step 1: Initialize variables
    strongest_extension = extensions[0]
    strongest_strength = sum(1 for c in strongest_extension if c.isupper()) - sum(1 for c in strongest_extension if c.islower())

    # Step 2: Loop through all extensions
    for extension in extensions[1:]:
        current_strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        if current_strength > strongest_strength or (current_strength == strongest_strength and extensions.index(extension) < extensions.index(strongest_extension)):
            strongest_extension = extension
            strongest_strength = current_strength

    # Step 3: Format the result
    result = f"{class_name}.{strongest_extension}"

    # Step 4: Return the result
    return result