# class Motor Bike


class MotorBike:

    def __init__(self, name, spped):
        self.name = name
        self.spped = spped

    def increse_speed(self, how_much):
        self.spped += how_much

    def decrese_speed(self, how_much):
        self.spped += how_much

    pass


honda = MotorBike('Honda', 80)
ducati = MotorBike('Ducati', 250)


motors = (honda, ducati)


def show_motors():
    for m in motors:
        print(m.name)
        print(m.spped)


show_motors()


honda.increse_speed(160)
ducati.increse_speed(200)

show_motors()

honda.decrese_speed(29)
ducati.decrese_speed(38)

show_motors()



#honda.spped = 80
#ducati.spped = 250




