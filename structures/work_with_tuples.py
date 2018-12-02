def create_todeshini():
    return 'Artur', 'Todeschini', 1977


artur = create_todeshini()
print(type(artur))
print(artur)
first, last, year = artur
print(f'first is {first}')
print(f'last is {last}')
print(f'year is {year}')
print(len(artur))

print(artur[0])
print(artur[1])
print(artur[2])

# when I use tuples I can change de values of position
# artur[1] = 'Crestani'  # this raise a Error