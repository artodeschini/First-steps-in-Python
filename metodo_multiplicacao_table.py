
def tabela_multiplicacao_numero_start_end(n, start = 1, end = 10) :
    for i in range(start, end) :
        print(f'{n} * {i} = {n * i}')


def tabela_multiplicacao_numero(n) :
    tabela_multiplicacao_numero_start_end(5)

tabela_multiplicacao_numero(5)
print()
tabela_multiplicacao_numero_start_end(5, 3, 8)