print('digite a quantidade de acoes')
n = int( input() )

print('digite as acoes')
actions = input().split()

a = 0
b = 0

for action in actions :
    if action == '1' :
        # ternarios em python
        a = 1 if a == 0 else 0
    elif action == '2' :
        a = 1 if a == 0 else 0
        b = 1 if b == 0 else 0