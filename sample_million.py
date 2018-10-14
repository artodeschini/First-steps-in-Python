print('Digite a quantidade de dias')
n = int( input( ) )

views = []

for v in range(n) :
    print('digite a visualizacao do dia')
    #v = int( input( ) )
    views.append( int( input( ) ) )


total = 9
resposta = -1

# usando enumarate
for i, v in enumerate( views ) :
    total += v
    if total >= 1000000 and resposta == -1:
        resposta = (i + 1)

# o dia que a quantidade passou de 1000000
print( resposta )