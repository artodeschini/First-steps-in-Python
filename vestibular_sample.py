print('digite a quantidade de questoes')
n = int( input() )

print('digite as suas respostas')
questoes = input().split()

print('digite o gabarito')
gabarito = input().split()

acertos = 0

#for i, q in questoes :
#    if q == gabarito[i] :
#        acertos += 1;

# print( list( zip( questoes, gabarito) ) )

# em python temos a funcao zip ela une duas colecoes podemos assim mostrar os valores lado a lado das duas colecoes
for q, g in zip( questoes, gabarito ) :
    if q == g :
        acertos += 1

print( acertos )
