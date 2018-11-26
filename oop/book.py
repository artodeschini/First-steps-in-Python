# class Book
class Book:

    #contrutor of Book
    def __init__(self, name, copies=0):
        self.name = name
        self.copies = copies

    def increse_copies(self, how_much):
        self.copies += how_much

    def decrese_copies(self, how_much):
        self.copies -= how_much

    pass


# hf = Book()
# bible = Book()
# tp = Book()

#hf.name = 'Head in First'
#bible.name  = 'Bible'
#tp.name  = 'Thinking in Python'


hf = Book('Head in First')
bible = Book('Bible', 12)
tp = Book('Thinking in Python', 2)

books = {hf, bible, tp}


def show_books():
    for i,b in enumerate(books):
        print(f'the {i + 1} book is {b.name} number of copies {b.copies}')


show_books()

for b in books:
    b.increse_copies(15)

show_books()

for b in books:
    b.decrese_copies(5)

show_books()
