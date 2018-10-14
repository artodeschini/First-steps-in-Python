# while

i = 0

while i < 6 : # condição
    print( i )
    i = i + 1

print('fim do while')

# for in em uma lista de valores
for i in [ 1, 2, 3, 4, 5 ] :
    print( i )

print('fim do for de uma list')

# for in em um range de valores imprime de 1 até 5, pois o segundo valor nao está incluso no interval
for i in range(1, 6) :
    print(i)

print('fim do for em um range')

# podemos utilizar um terceiro argumento em range para incrementar o range de dois em dois no exemplo
for i in range(1, 10, 2) :
    print(i)

# range nao é uma list
# observacao quando queremos um range de 0 até outro valor podemos omitir o primeiro argumento
r = range(10)
print( type( r ) )
print( r )

# range é um interval para transformar em list
aList = list(r)
print( aList )
