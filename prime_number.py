def is_prime(number):
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
        return True

def sum_up_n(number):
    sum_up = 0
    for n in range(1,number + 1):
        sum_up += n
    return sum_up

def print_triagule_of_number(number):
    line = ''
    for x in range(1, number + 1):
        line += '\n'
        for y in range(1, x + 1):
            line += ' ' + str(y)
    return line

def sum_of_divisiors(number):
    _sum = 0;
    for n in range(1, number):
        if number % n == 0:
            _sum += n
    return _sum


n = int(input('Digit a number\n'))

message = f'{n} is '
b = is_prime(n)
if b:
    message += 'prime'
else:
    message += 'not prime'
print(message)

sum_up = sum_up_n(n)
message = f'The sum until de {n} is {sum_up}'
print(message)

print(print_triagule_of_number(n))
_sum_divisors = sum_of_divisiors(n)
print(f'The sum of divisor of {n} is {_sum_divisors}')