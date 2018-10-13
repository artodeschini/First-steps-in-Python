
print("Digite tres x zero ou um")
a , b , c = input().split()

ganhador = None

if a != b and a != c :
    ganhador = 'a'
elif b != a and b !=c :
    ganhador = 'b'
elif c != a and c != b :
    ganhador = 'c'
else:
    ganhador = '*'

print(ganhador)