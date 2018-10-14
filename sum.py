# Faça um programa que leia dois números inteiros digitados pelo teclado e imprima a soma deles.

# Entrada
# A entrada consiste de dois números inteiros
# X
# e
# Y
# , um em cada linha.

# Saída
# A saída do seu programa deve ser um inteiro
# S
# , representando a soma de
# X e Y.

#| Exemplos de Entrada | Exemplos de Saida | | -------------------------- |:-------------:| | 3
# 4 | 7 | | 1
# 1 | 2 |


# este exemplo le duas variaveis
# o comando imput é que realiza a entrada que é sempre por padrao uma string
print('Digite o primeiro numero')
n1 = input()


print('Digite o egundo numero')
n2 = input()

# convertendo para inteiro para nao concatenar e poder calcular a soma
n1 = int(n1)
n2 = int(n2)

# utilizando .format para apresentar o resultado
print('A soma de {} + {} = {} '.format(n1,n2, (n1 + n2 ) ) )


print('Digite dois numeros separados por espaco')

# o comando imput sempre pega uma string linha inteira
# aqui separamos os dois valores separados por espaco nas variaveis
n1 , n2  = input().split()

n1 = int(n1)
n2 = int(n2)

print('A soma de {} + {} = {} '.format(n1,n2, (n1 + n2 ) ) )

