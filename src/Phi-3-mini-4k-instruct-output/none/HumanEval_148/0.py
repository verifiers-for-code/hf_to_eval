def bf(planet1, planet2):
    """
    Returns a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2, sorted by proximity to the sun.
    """
    # Define the planets and their order in the solar system
    planets = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }
    
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get the positions of planet1 and planet2
    pos1 = planets[planet1]
    pos2 = planets[planet2]
    
    # Find the planets between planet1 and planet2
    planets_between = [planet for planet, pos in planets.items() if pos > pos1 and pos < pos2]
    
    # Sort the planets by their position in the solar system
    planets_between.sort(key=lambda planet: planets[planet])
    
    # Return the planets as a tuple
    return tuple(planets_between)