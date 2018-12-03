class Book:

    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))

    def add_review(self, review):
        self.reviews.append(review)


class Review:

    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id, self.description, self.rating))


book = Book(1, 'OOP whith python', 'Artur')
print(type(book))
print(book)

review1 = Review(10, 'Great book', 100)
print(type(review1))
print(review1)

book.add_review(review1)

print(book)

book.add_review(Review(101, 'Another', 5.0))

print(book)

