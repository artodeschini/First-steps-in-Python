numbers = ['Zero', 'One', 'Two',
           'Three', 'Four', 'Five',
           'Six', 'Seven', 'Eight',
           'Nine']

print(type(numbers))
print(len(numbers))
print(numbers)

# get a specific position
print(numbers[2])

# get a slicing of a list [init:end]
print(numbers[2:6]) # look the second is excluded same is a range

# if not use the first element assume 0 [:end]
print(numbers[:6])

# if not use the second element assume the last [start:]
print(numbers[3:])

# if I use three arguments the first is start, second delimiter, and three steep
print(numbers[0:9:2]) # print only even numbers

print(numbers[1::2]) # print only odd numbers

print(numbers[3::3]) # print multiples of three

# print list reverse order
print(numbers[::-1])

# print list reverse order three in three elements
print(numbers[:1:-3])

# alter list in position 3 to 6
numbers[3:7] = [3,4,5,6]
print(numbers)

del numbers[3:7]

print(numbers)