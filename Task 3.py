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

    def update_population(self, new_population):
        self.population = new_population
        print("Кількість жителів країни оновлено.")

    def add_city(self, new_city):
        self.cities.append(new_city)
        print(f"Додано нове місто: {new_city}")

country = Country("Україна", "Європа", 38000000, "+380", "Київ", ["Львів", "Одеса", "Харків", "Миколаїв"])


print("Інформація про країну:")
country.display_info()

country.update_population(35000000)

country.add_city("Дніпро")

print("\nОновлена інформація про країну:")
country.display_info()
