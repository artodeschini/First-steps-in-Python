print('Hello World')

list = []

integer = 1;
double = 1.5
string = 'a word'
boolean1 = True;
boolean2 = False;

list.append(integer)
list.append(double)
list.append(string)
list.append(boolean1)
list.append(boolean2)

for value in list :
    print(value)

# o comando print pode ser sobrecarregado com um paraetro
print('A soma de 2 + 5 é igual a: ' , 7 )
# o comando print pode usar .format() dessa forma ele vai substituir os parametros nas ocorrencias de {}
print('A soma de 2 + 5 é igual a: {} '.format(7) )

n1 = 7
n2 = 4
print('A soma de {} + {} é igual a: {}'.format(n1,n2, (n1+n2) ) )

print('A divisao de {} + {} é igual a: {}'.format(n2,n1, (n2/n1) ) )
# definindo a saida com duas casas decimais
print('A divisao de {} + {} é igual a: {:.2f}'.format(n2,n1, (n2/n1) ) )
# definido a saida com só a parte inteira
print('A divisao de {} + {} é igual a: {:.0f}'.format(n2,n1, (n2/n1) ) )

# o comando print por padrao quebra a as linhas
print('linha 1')
print('linha 2')

# para faze-lo não quebrar posso passar como parametro , end = ' '
print('linha 1', end = ' ')
print('linha 2')

