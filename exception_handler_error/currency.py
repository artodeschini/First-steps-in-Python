class CurrencyError(Exception):

    def __init__(self, message):
        super().__init__(message)

    pass


class Currency:

    def __init__(self, currency,amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception("Currencies not match")
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)


value1 = Currency('USD', 20)
value2 = Currency('USD', 30)

try:
    print(value1 + value2)
except Exception as e1:
    print(e1)

value3 = Currency('USD', 10)
value4 = Currency('REAL', 30)

try:
    print(value3 + value4)
except Exception as e2:
    print(e2)
    print(type(e2))
