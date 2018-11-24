# class Book
class Book:
    pass

hf = Book()
bible = Book()
tp = Book()

hf.name = 'Head in First'
bible.name  = 'Bible'
tp.name  = 'Thinking in Python'

books = { hf, bible, tp }

for b in books:
    print( b.name )