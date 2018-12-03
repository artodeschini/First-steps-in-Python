class Fan:

    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.on = False
        self.speed = 0

    def switch_on(self):
        self.on = True
        self.speed = 3

    def switch_off(self):
        self.on = False
        self.speed = 0

    def increase_speed(self, speed):
        self.speed += speed
        self.on = True

    def decrease_spped(self, speed):
        self.speed -= speed
        if self.speed <= 0:
            self.on = False
            self.speed = 0

    # this method is same of toString in java
    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.on, self.speed))


my_fan = Fan('Manufacture 1', 5, 'Green')
print(my_fan)

my_fan.switch_on()
print(my_fan)

my_fan.switch_off()
print(my_fan)
