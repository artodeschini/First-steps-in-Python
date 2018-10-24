print('Digite um numero de 1 a 10 ')
n = int(input())

for i in range(1,11) :
	print('{0} * {1} = {2}'.format( n, i, ( n * i ) ) )