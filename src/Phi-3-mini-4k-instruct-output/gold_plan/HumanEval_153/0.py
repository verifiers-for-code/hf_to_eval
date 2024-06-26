def Strongest_Extension(class_name, extensions):
    # Step 1: Initialize variables
    strongest_extension = extensions[0]
    strongest_strength = calculate_strength(strongest_extension)

    # Step 2: Iterate through all extensions
    for extension in extensions[1:]:
        extension_strength = calculate_strength(extension)
        # Compare the strength with the current strongest
        if extension_strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = extension_strength

    # Step 3: Format the result
    result = f"{class_name}.{strongest_extension}"

    return result

def calculate_strength(extension):
    """Calculate the strength of an extension."""
    uppercase_count = sum(1 for char in extension if char.isupper())
    lowercase_count = sum(1 for char in extension if char.islower())
    return uppercase_count - lowercase_count