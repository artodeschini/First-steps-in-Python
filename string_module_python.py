import string

print(string.ascii_letters)

print(string.ascii_lowercase)

print(string.ascii_uppercase)

print(string.digits)

print(string.punctuation)

print(string.hexdigits)

print(string.whitespace)

print(string.printable)

print( 'a' in string.ascii_letters ) # return boolean value

for c in string.ascii_uppercase :
    print(c)

myString = 'A simple sample of String'

separate = myString.split(' ')
print(separate)

lines = 'A\nsimple\nsample\nof\nString'.splitlines() # splitlines use split with \n in argument
print(lines)


