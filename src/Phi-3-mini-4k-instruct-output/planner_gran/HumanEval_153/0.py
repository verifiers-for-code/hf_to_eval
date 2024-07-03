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
    For example, if you are given "Slices" as the class and a list of
    the extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    
    1. Define the function Strongest_Extension with two parameters: class_name and extensions
       - class_name is a string representing the name of the class
       - extensions is a list of strings representing the names of the extensions
    
    2. Initialize variables to keep track of the strongest extension and its strength
       - strongest_extension: an empty string to store the name of the strongest extension
       - strongest_strength: an integer to store the strength of the strongest extension (initially 0)
    
    3. Iterate through each extension in the list of extensions:
       a. Calculate the strength of the current extension:
          - Calculate the number of uppercase letters in the extension's name (CAP)
          - Calculate the number of lowercase letters in the extension's name (SM)
          - Calculate the strength as CAP - SM
       b. Compare the strength of the current extension with the strongest strength found so far:
          - If the current strength is greater than the strongest strength:
             - Update the strongest_extension with the current extension's name
             - Update the strongest_strength with the current strength
    
    4. After processing all extensions, return the strongest extension in the desired format:
       - Use string formatting to combine the class name and the strongest extension with a dot in between
    
    Additional implementation details:
    - Use a loop to iterate through the list of extensions
    - Use the appropriate string methods to count uppercase and lowercase letters
    - Use conditional statements to compare and update the strongest extension and its strength
    - Ensure that the function handles empty input lists and edge cases correctly"""
    
    strongest_extension = ""
    strongest_strength = 0
    
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    
    return f"{class_name}.{strongest_extension}"