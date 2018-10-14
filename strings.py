# python permite criar string com aspas simpes ou duplas

s1 = 'uma palavra ou uma frase'
s2 = "outra string"

print( type( s1 ) )

# pegan uma poiscao da string
print( s1[0] )

# diferencas para outras linguagens uma posicao da string é outra string
print( type( s1[0] ) )

# isso vai gerar um erro
#s1[0] = 'x'

print('a quantidade de letras é ' , len( s1 ) )

# alterar uma ocorrencia na string
print( s1.replace('palavra', 'outra' ) )
# observe que s1 nao foi modificado
print( s1 )

# funcao split
#
s3 = s1.split('a')
print( s3 )

# in verifica se contem dentro da colecao
print( 'a' in s1 )

