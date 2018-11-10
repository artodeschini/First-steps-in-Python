message = 'Digit the {0} numero'
menu = 'Choose a operation\n1 to sum\n2 to subtract\n3 to multiplication\n4 Division\n5 pow\n6 sair'

def get_a_number( select ) :
    return int( input( message.format( select ) ) )



op = int( input( menu ) )
while op != 6 :

    if op == 1 :
        n1 = get_a_number( 1 )
        n2 = get_a_number( 2 )
        print( n1 + n2 )

        op = int(input(menu))


    elif op == 2 :
        n1 = get_a_number(1)
        n2 = get_a_number(2)
        print(n1 - n2)

        op = int(input(menu))

    elif op == 3 :
        n1 = get_a_number(1)
        n2 = get_a_number(2)
        print(n1 * n2)

        op = int(input(menu))


    elif op == 4:
        n1 = get_a_number(1)
        n2 = get_a_number(2)
        print(n1 / n2)

        op = int(input(menu))


    elif op == 5:
        n1 = get_a_number(1)
        n2 = get_a_number(2)
        print(n1 ** n2)

        op = int(input(menu))

    else:
        print('you not digit a valid option')
        op = int(input(menu))