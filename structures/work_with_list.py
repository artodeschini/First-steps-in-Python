# a sample of list
# to create a list in python is very simple
# put values in square bracket start '[' and end ']'
makes = [10, 20, 30]
print(type(makes))


def show_index_of_a_element(element):
    print('The index of 30 is {0}'.format(makes.index(element)))


def calcule_makes_avg():
    return sum(makes)/len(makes)


def show_makes():
    for i, m in enumerate(makes):
        print(f'The {i+1} is {m}')


show_makes()
print(calcule_makes_avg())
# show the max value
print(max(makes))
# show the min value
print(min(makes))
print('The index of 30 is {0}'.format(makes.index(30)))

print('Add one more in makes ---> 40')
makes.append(40)

show_makes()
print(calcule_makes_avg())
# show the max value
print(max(makes))
# show the min value
print(min(makes))
print(len(makes))

makes.insert(1, 15)
print('The index of 30 is {0}'.format(makes.index(30)))
show_index_of_a_element(30)
print(len(makes))

show_makes()

makes.remove(15)
print('The index of 30 is {0}'.format(makes.index(30)))
show_index_of_a_element(30)
print(len(makes))