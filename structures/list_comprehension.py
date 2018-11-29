numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

print(even_numbers)
print(odd_numbers)

text_number = ['Zero', 'One', 'Two','Three', 'Four', 'Five','Six', 'Seven', 'Eight','Nine']

for n in text_number:
    if len(n) == 4:
        print(n)

# or
extract = [n for n in text_number if len(n) == 4]
print(extract)