# a list apend and pop is same a FIFO stack
stack = []

queue = []


def show_elements_of_queue():
    print('\nprint a queue :')
    for i, n in enumerate(queue):
        print(f'queue[{i}] = {n}')


def show_elements_of_stack():
    print('\nprint a stack :')
    for i, n in enumerate(stack):
        print(f'stack[{i}] = {n}')


print("sample a stack")

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

show_elements_of_stack()

last = stack.pop()
print(f'call pop and remove the last element {last}')
# remove the last element a list


show_elements_of_stack()

print("\nsample a queue")

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

show_elements_of_queue()

first = queue.pop(0)
print(f'call pop and remove the first element {first}')

show_elements_of_queue()


