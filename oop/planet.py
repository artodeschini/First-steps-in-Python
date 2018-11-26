class Planet:

    def rotate(self):
        print('Rotate')

    def revolve(self):
        print('Revolve')

    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()


    pass


earth = Planet()
earth.name = 'Earth'

venus = Planet()
venus.name = 'Venus'

planets = {venus, earth}


for i, p in enumerate(planets):
    print(f'The {i +1} planet is {p.name}')
    p.rotate_and_revolve()