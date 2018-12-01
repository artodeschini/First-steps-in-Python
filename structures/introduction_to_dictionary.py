# dictionary is a key value same as map in java
occurrences = dict(a=1, b=2, c=3, d=4)
print(type(occurrences))
print(occurrences)

# I can get a element by a key
element = occurrences['a']
print(element)

# add a element
occurrences['e'] = 5
print(occurrences)

# try to get a key not exist raise a KeyError
#occurrences['f'] # note I not inicialize in my dictionary a element with key f

# I can get element with method get
other = occurrences.get('b')
print(other)

# note if I try get a element with method get not raise a KeyError
test = occurrences.get('f')  # this not raise Error
print(test)  # but test is None same is null in java

test = occurrences.get('a', 10)  # this key 'a' exist in my dictionary
print(test)  # the value is 1

test = occurrences.get('f', 10)  # this key 'f' not exist in my dictionary the second element is same a defaul value
print(test)  # the value of test is 10

# to get the keys of a dictionary use the method 'keys'
print(occurrences.keys())

# to get all values of a dictionary use the method 'values'
print(occurrences.values())

# to get the pair of key values use the method 'items'
print(occurrences.items())

for key, value in occurrences.items():
    print(f'{key} = {value}')

# to remove a element of dictionary
del occurrences['e']

print(occurrences.items())