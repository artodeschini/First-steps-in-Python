class Country:
    pass

us = Country()
uk = Country()
br = Country()
it = Country()

uk.name = 'United Kingdon'
uk.capital = 'London'

us.name = 'United States'
us.capital = 'Washington'

br.name = 'Brasil'
br.capital = 'Brasilia'

it.name = 'Italy'
it.capital = 'Rome'

countries = ( uk, us, br, it )

for c in countries:
    print(f'the capital of {c.name} is {c.capital}')

