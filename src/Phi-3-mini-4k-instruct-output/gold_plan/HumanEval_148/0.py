def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closest to the Sun is Mercury,
    the next one is Venus, then Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2.
    The function should return a tuple containing all planets whose orbits are
    located between the orbit of planet1 and the orbit of planet2, sorted by
    the proximity to the sun.
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names.
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

    Action Plan:
    1. Create a tuple of planet names in order from closest to farthest from the Sun.
    2. Check if both planet1 and planet2 are in the tuple of planet names and are different.
       If not, return an empty tuple.
    3. Find the index of planet1 and planet2 in the tuple of planet names.
    4. Determine which planet is closer to the Sun by comparing their indices.
    5. Extract the planets between the two input planets:
       - If planet1 is closer, return planets from (index of planet1 + 1) to (index of planet2).
       - If planet2 is closer, return planets from (index of planet2 + 1) to (index of planet1).
    6. Return the result as a tuple.
    '''
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planets or planet2 not in planets or planet1 == planet2:
        return ()
    index1, index2 = planets.index(planet1), planets.index(planet2)
    if index1 < index2:
        return planets[index1 + 1:index2]
    else:
        return planets[index2 + 1:index1]