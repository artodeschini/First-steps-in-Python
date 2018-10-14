# para criar uma lista vazia
myList = []

# para criar uma lista com valores observe que o tipo das variaveis podem ser diferentes na lista
anotherList = [ 1, 2, 3, 4 , 'word', 1.5 ]

# para checar o tipo da variavel
print( type( myList ) )

myList.append( 1 )

print( myList )
print( anotherList )

# para acessar uma posição especifica da lista
anotherList[0] = 999

print(anotherList)

# para visualizar o ultimo elemento de uma lista use -1
print( anotherList[-1])

# para deletar um elemento da lista
del anotherList[0]

print( anotherList )

# mostrar elementos entre um range em uma list
print( anotherList[0:3])