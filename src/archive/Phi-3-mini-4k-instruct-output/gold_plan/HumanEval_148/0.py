def bf(planet1, planet2):
    """
    Returns a tuple of planets whose orbits are located between the orbit of planet1 and planet2, sorted by proximity to the sun.
    """
    # Step 1: Create a tuple of planet names in order from closest to farthest from the Sun.
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    # Step 2: Check if both planet1 and planet2 are in the tuple of planet names and are different.
    if planet1 not in planets or planet2 not in planets or planet1 == planet2:
        return ()

    # Step 3: Find the index of planet1 and planet2 in the tuple of planet names.
    index_planet1 = planets.index(planet1)
    index_planet2 = planets.index(planet2)

    # Step 4: Determine which planet is closer to the Sun by comparing their indices.
    if index_planet1 < index_planet2:
        start_index = index_planet1 + 1
    else:
        start_index = index_planet2 + 1

    # Step 5: Extract the planets between the two input planets.
    planets_between = planets[start_index:index_planet2]

    # Step 6: Return the result as a tuple.
    return tuple(planets_between)