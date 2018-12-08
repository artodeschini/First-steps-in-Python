class Person:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class Student:

    def __init__(self, name, identify):
        self.name = name
        self.identify = identify


s1 = Student('Artur', 1)
# id is same of the hashcode in java
h1 = id(s1)
print(h1)

s2 = Student('Manu', 2)
h2 = id(s2)
print(h2)

if s1 == s2:
    print('equals')
else:
    print('not equals')

# is check if the same hash
b = s1 is s2
print(f's1 is the same s1 {b}')

p1 = Person('Artur')
p2 = Person('Manu')
p3 = Person('Artur')
p4 = p2

print(p1 == p3)

