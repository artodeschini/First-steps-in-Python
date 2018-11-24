# class Book
class Book:
    def __init__(self, name):
        self.name = name

# hf = Book()
# bible = Book()
# tp = Book()

#hf.name = 'Head in First'
#bible.name  = 'Bible'
#tp.name  = 'Thinking in Python'

hf = Book('Head in First')
bible = Book('Bible')
tp = Book('Thinking in Python')

books = { hf, bible, tp }

for i,b in enumerate(books):
    print( f'the {i + 1} book is {b.name} ')