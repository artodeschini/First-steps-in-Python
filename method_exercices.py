# write a method printNumbers(n) that print a number to 1 to n

def print_numbers(n) :
    for i in range(1, (n +1) ) :
        print(i)


print_numbers(5)

# write a method print_squares_of_numbers(n) that print the squares of sucessive integer from 1 to n

def print_squares_of_numbers(n) :
    for i in range(1, (n +1) ) :
        print(i * i )


print_squares_of_numbers(10)

# definindo um valor padrao para os argumento de metodos
def print_string_of_times(str = 'Hello World', no_of_times = 1) :
    for i in range(1, no_of_times + 1) :
        print(str)

print_string_of_times()
print_string_of_times('Python')
print_string_of_times('Python3',3)