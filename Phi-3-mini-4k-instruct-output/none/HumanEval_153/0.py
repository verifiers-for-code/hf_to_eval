
    def calculate_strength(extension):
        """Calculate the strength of an extension."""
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        return cap - sm

    def Strongest_Extension(class_name, extensions):
        """Find the strongest extension and return a string in the format: ClassName.StrongestExtensionName."""
        strongest_extension = extensions[0]
        strongest_strength = calculate_strength(strongest_extension)
        
        for extension in extensions[1:]:
            extension_strength = calculate_strength(extension)
            if extension_strength > strongest_strength or (extension_strength == strongest_strength and extensions.index(extension) < extensions.index(strongest_extension)):
                strongest_extension = extension
                strongest_strength = extension_strength
                
        return f"{class_name}.{strongest_extension}"