print('Digite um numero de 1 a 10 ')
n = int(input())

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

for i in numbers :
	print('{0} * {1} = {2}'.format( n, i, ( n * i ) ) )