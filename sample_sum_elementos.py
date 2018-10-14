print('digite a quantidade de elementos')
n = int(input())

print('digite tres valores separados por espaços')
values = input().split()

# transformando os valores em inteiros
for i in range(len(values) ) :
    values[ i ] = int( values[ i ] )

soma = 0

# de maneira programatica faria assim
for element in values :
    soma += element

print( soma )

# em python podemos simplificar isso com a funcao sum que ira somar todos os elementos
print( sum( values ) )

print( sum( range(0,5) ) )