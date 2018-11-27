animals = ['Cat', 'Dog', 'Elephant', 'Bee']

print(len(animals))
print(type(animals))
print(animals)
#print(sum(animals)) raise TypeError str not += int
print(f'index 1 of aniemals {animals[1]}')

# to add one element in a list use append
animals.append('Fish')
print(animals)

animals.remove('Dog')
print(f'index 1 of aniemals {animals[1]}')
print(animals)

#animals[-1] raise IndexError

del animals[3] # del element fish
print(animals)

# to add two or more element use extends
animals.extend(['Giraffe', 'Horse']) # not split the char one to one
print(animals)

# when to use extend use always a list [] in your attr
animals.extend('Lion') # if you not use a list this occur create new 4 position on for char
print(animals)

animals += ['Kangarro', 'Spider']
print(animals)

animals = animals + ['Monkey', 'Star Fish']
print(animals)

animals.append( 10 )

print(animals)