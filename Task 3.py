# Створіть клас «Країна».
# Збережіть у класі: назву країни, назву континенту, кількість жителів країни,
# телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
print("Завдання №3")


class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def display_info(self):
        print("Назва країни: ", self.name)
        print("Континент: ", self.continent)
        print("Кількість жителів: ", self.population)
        print("Телефонний код країни: ", self.phone_code)
        print("Столиця: ", self.capital)
        print("Міста країни:")
        for city in self.cities:
            print("  -", city)

    def add_city(self, new_city):
        self.cities.append(new_city)
        print(f"Додано нове місто: {new_city}")

    def __str__(self):
        return f"{self.name}, {self.continent}, {self.population}, {self.phone_code}, {self.capital}, {self.cities}"

    def __eq__(self, other):
        return (
                isinstance(other, Country) and
                self.name == other.name and
                self.population == other.population
        )
country1 = Country("Україна", "Європа", 38000000, "+380", "Київ", ["Львів", "Одеса", "Харків", "Миколаїв"])
country2 = Country("Німеччина", "Європа", 83000000, "+49", "Берлін", ["Мюнхен", "Гамбург", "Франкфурт"])

if country1 == country2:
    print(f"{country1.name} та {country2.name} - мають однакову кількість населення країни.")
else:
    print(f"{country1.name} та {country2.name} - мають різну кількість населення країни.")

print("\nІнформація про країну у вигляді рядка:")
print(str(country1))
print(str(country2))
