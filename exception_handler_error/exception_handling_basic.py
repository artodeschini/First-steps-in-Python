try:
    # digite a number != of 0 and a char
    i = int(input('Digite a number'))
    j = 10/i
    values = [1, '1']
    sum(values)

except ZeroDivisionError:
    print('ZeroDivisionError')
    j = 0

except TypeError:
    print('TypeError')


print(j)
print('End')