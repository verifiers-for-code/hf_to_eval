
    def compare_one(a, b):
        # Check if both inputs are of the same type
        if type(a) != type(b):
            return None
        
        # If both inputs are strings, try to convert them to floats
        if isinstance(a, str) and isinstance(b, str):
            try:
                a = float(a.replace(",", "."))
                b = float(b.replace(",", "."))
            except ValueError:
                return None
        
        # Compare the values
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None