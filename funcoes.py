
def calculos( x , y ) :
    resp = x ** 2 + y ** 2

    return resp, x ** 2, y ** 2


# o retorno de uma funcao é uma tupla e nao pode ser alterado
print(  type(calculos( 5 , 2) ) )

print( calculos( 5 , 2) )
# acessando so o primeiro retorno do resultado da chamada da funcao
print( calculos( 5 , 2)[0] )

# forma de pegar os resultados de uma funcao
# * _ descarta os demais retornos
calculo , x_quadrado, * _ = calculos( 5, 2)

print( calculo )
print( x_quadrado )