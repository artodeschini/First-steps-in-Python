try:
    # Business locig
    i = 1
    j = 10/i
    values = [1,2]
    sum(values)
except TypeError:
    print('TypeError')
    j = 10
except ZeroDivisionError:
    print('ZeroDivisorError')
    j = 0
else:
    print('Else') # else execute when Exception not throw
finally:
    print('Finally') # all finally is call

print(j)
print('End')

try:
    1/1
finally:
    print('This is possible')

#try:
#    1/0
#else: # to use else I need one except
#    print('no possible')