class Country:

    # this is a constructor of the class
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    # this is same with toString in Java
    def __repr__(self):
        return repr((self.name, self.population, self.area))


india = Country('India', 1200, 100)
china = Country('China', 1400, 200)
eua = Country('United States', 120, 300)

countries = [india, china, eua]

print(countries)

countries.append(Country('Russia', 80, 500))

print(countries)

print(countries[len(countries):0: -1])