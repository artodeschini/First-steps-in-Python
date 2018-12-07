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

try:
    10/0
except BaseException:
    print('BaseException is the first Exception to handler')
    print('BaseException inherit to object')

# try:
#     10/0
# except object:
#     print('no work because no catch handler')

print('sample with multiple Exception')

try:
    10/0
except (ZeroDivisionError,TypeError,BaseException) as e1:
    print(type(e1))
    print(e1)
    print('multiple exception')

values = [1,'1']

try:
    sum(values)/0
except (ZeroDivisionError,TypeError,BaseException) as e2:
    print(type(e2))
    print(e2)
    print('multiple exception')