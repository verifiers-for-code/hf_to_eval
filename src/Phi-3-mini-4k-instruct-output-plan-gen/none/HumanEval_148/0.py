
def bf(planet1, planet2):
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

    # Check if the input planets are valid
    if planet1 not in planets or planet2 not in planets:
        return ()

    # Get the positions of the input planets
    pos1 = planets[planet1]
    pos2 = planets[planet2]

    # Find the planets between the two input planets
    planets_between = []
    for planet, pos in planets.items():
        if pos > pos1 and pos < pos2:
            planets_between.append(planet)

    # Sort the planets by their proximity to the sun
    planets_between.sort(key=lambda x: planets[x])

    return tuple(planets_between)