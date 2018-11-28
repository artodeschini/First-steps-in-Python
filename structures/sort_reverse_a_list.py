import string

numbers = ['Zero', 'One', 'Two',
           'Three', 'Four', 'Five',
           'Six', 'Seven', 'Eight',
           'Nine']

print(type(numbers))
print(len(numbers))

print(numbers)

# reverse order to element of a list
numbers.reverse()
print(numbers)

# just to restore the list to original
numbers.reverse()
print(numbers)

# We can use reversed but I will need a iterator to show elements
# this is a difference to .reverse() to list and reversed()
# but not modify the original list
for n in reversed(numbers):
    print(n, end=' ')
print()

# order element to alphabetic order
numbers.sort()
print(numbers)

letters = []
letters.extend(string.ascii_uppercase)
print(letters)
letters.reverse()
print(letters)
letters.sort()
print(letters)

# start numbers again
numbers = ['Zero', 'One', 'Two',
           'Three', 'Four', 'Five',
           'Six', 'Seven', 'Eight',
           'Nine']

# sorted is same with reversed but not modify the original list
for n in sorted(numbers):
    print(n, end=' ')
print()

print(numbers)

for n in sorted(numbers, key=len):
    print(n, end=' ')
print()

for n in sorted(numbers, key=len, reverse=True):
    print(n, end=' ')
print()