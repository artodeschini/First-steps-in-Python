# class Motor Bike

class MotorBike:
    def __init__(self, name, spped):
        self.name = name
        self.spped = spped

honda  = MotorBike('Honda', 80)
ducati = MotorBike('Ducati', 250)

motors = ( honda, ducati )

for m in motors:
    print(m.name)
    print(m.spped)

#honda.spped = 80
#ducati.spped = 250




