i = 1
print( type( i ) )

i + 1;

print( i )

i += 1

print( i )

# python nao aceita pre e pos incremento
# i++ isso da um erro de sintase

a = 10
# isso nao da um erro mas nao incrementa a variavel

++a
print( a )

# a divisao de dois numeros inteiros resulta em um float
myDouble = 5 / 2
type(myDouble)
print( myDouble )

# a divisao de dois numeros inteiros para resulta em um int use dois '//'
myInteger = 5 // 2
type(myInteger)
print( myInteger )

# para usar potencia
# use a função pow(base, elevado)
print( pow(2,3) )
print( 2 ** 3 )

# para trucar un valor float em int
print( int(5.6) )

# para realizar arredondamento use a função round
print( round(5.6) )
print( round(5.5) )
print( round(5.4) )

# arredodament com numero de casa decimais
print( round( 1.2345, 2) )

#para converter um int em um float
print(float(5))