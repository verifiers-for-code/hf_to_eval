def get_extension_strength(extension):
    """Calculate the strength of an extension."""
    uppercase_count = sum(1 for c in extension if c.isupper())
    lowercase_count = sum(1 for c in extension if c.islower())
    return uppercase_count - lowercase_count

def find_strongest_extension(class_name, extensions):
    """Find the strongest extension."""
    strongest_extension = None
    strongest_strength = float('-inf')
    for extension in extensions:
        strength = get_extension_strength(extension)
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    return strongest_extension

def Strongest_Extension(class_name, extensions):
    """Return the strongest extension in the format 'ClassName.StrongestExtensionName'."""
    strongest_extension = find_strongest_extension(class_name, extensions)
    if strongest_extension:
        return f"{class_name}.{strongest_extension}"
    else:
        return None