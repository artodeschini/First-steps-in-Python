# list is a structures that content duplicates
aList = [1, 2, 3, 4, 3, 2, 1]
print(type(aList))
print(aList)

# set has not duplicates
aSet = set(aList) # remove the duplicates
print(type(aSet))
print(aSet)

# set not permit duplicate
aSet.add(4)
print(aSet)

aSet.add(5)
aSet.add(0)

print(aSet)
aSet.remove(5)
print(aSet)

# this not possible get a element to index
# set not support index
#print(aSet[0]) raise a TypeError

# to know that a value is 'in' a set
print(0 in aSet)
print(9 in aSet)

# to know a length of a set use len
print(len(aSet))

# I can use sum, max and min with a set
print(sum(aSet))
print(max(aSet))
print(min(aSet))

# create a set to 1 to 5
number_1_to_5 = set(range(1,6))
print(type(number_1_to_5))
print(number_1_to_5)

# create another set to 4 to 10
number_4_to_10 = set(range(4,11))

# to union two set use |
new_set = number_1_to_5 | number_4_to_10
print(type(new_set))
print(new_set)

# to find the intersection between two set
intersection = number_1_to_5 & number_4_to_10
print(type(intersection))
print(intersection)

# to get a set one minus another
minus = number_4_to_10 = number_1_to_5
print(type(minus))
print(minus)