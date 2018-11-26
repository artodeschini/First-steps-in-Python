# a sample of list
makes = [10, 20, 30]
print(type(makes))


def calcule_makes_avg():
    return sum(makes)/len(makes)


def show_makes():
    for i, m in enumerate(makes):
        print(f'The {i+1} is {m}')


show_makes()
print(calcule_makes_avg())

print('Add one more in makes ---> 40')
makes.append(40)

show_makes()
print(calcule_makes_avg())