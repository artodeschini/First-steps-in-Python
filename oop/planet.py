class Planet:
    pass


earth = Planet()
earth.name = 'Earth'

venus = Planet()
venus.name = 'Venus'

planets = {venus, earth}


for i, p in enumerate(planets):
    print(f'The {i +1} planet is {p.name}')