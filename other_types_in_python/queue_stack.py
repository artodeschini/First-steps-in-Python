from collections import deque

queue = deque(['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'])


def show_elements_in_queue():
    for i, v in enumerate(queue):
        print(f'Queue[{i}] has values {v}')


show_elements_in_queue()

# this is a FIFO First in First out
out = queue.pop()
print(out)

show_elements_in_queue()

queue.append('Add in last')
show_elements_in_queue()

# if I want to put in begin
queue.appendleft('Menus One')
show_elements_in_queue()