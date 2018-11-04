def parametro_nao_obrigatorio( msg = 'Ola' , print_times = 1) :
    for i in range(1, print_times + 1) :
        print( msg )

#caso queira imprimir Ola 3x
parametro_nao_obrigatorio( print_times = 3 )

print()

print('é diferente de ')
parametro_nao_obrigatorio( 3 )