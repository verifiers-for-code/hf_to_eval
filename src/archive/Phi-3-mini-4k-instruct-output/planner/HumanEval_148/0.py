def bf(planet1, planet2):
    """
    This function takes two planet names as strings planet1 and planet2, and returns a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2, sorted by the proximity to the sun.
    
    Args:
    planet1 (str): The name of the first planet.
    planet2 (str): The name of the second planet.
    
    Returns:
    tuple: A tuple containing the names of the planets whose orbits are located between the orbits of planet1 and planet2, sorted by proximity to the sun. Returns an empty tuple if either planet1 or planet2 is not a correct planet name.
    
    Examples:
    >>> bf("Jupiter", "Neptune")
    ("Saturn", "Uranus")
    >>> bf("Earth", "Mercury")
    ("Venus")
    >>> bf("Mercury", "Uranus")
    ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    # Define the order of the planets by proximity to the sun
    planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if both planet names are valid
    if planet1 not in planets_order or planet2 not in planets_order:
        return ()
    
    # Find the indices of the planets in the list
    planet1_index = planets_order.index(planet1)
    planet2_index = planets_order.index(planet2)
    
    # If planet1 comes after planet2, swap their indices
    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index
    
    # Return the planets between the two indices, sorted by proximity to the sun
    return tuple(sorted(planets_order[planet1_index+1:planet2_index]))