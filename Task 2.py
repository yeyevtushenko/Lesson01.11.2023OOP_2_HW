# Створіть клас «Місто».
# Збережіть у класі: назву міста, назву регіону, назву країни, кількість
# жителів у місті, поштовий індекс міста, телефонний код міста.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
print("Завдання №2")


class City:
    def __init__(self, name, region, country, population, zipcode, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zipcode = zipcode
        self.phone_code = phone_code

    def display_info(self):
        print("Назва міста: ", self.name)
        print("Регіон: ", self.region)
        print("Країна: ", self.country)
        print("Кількість жителів: ", self.population)
        print("Поштовий індекс: ", self.zipcode)
        print("Телефонний код: ", self.phone_code)

    def update_population(self, new_population):
        self.population = new_population
        print("Кількість жителів оновлено.")

    def update_data(self, new_name, new_region, new_country, new_zipcode, new_phone_code):
        self.name = new_name
        self.region = new_region
        self.country = new_country
        self.zipcode = new_zipcode
        self.phone_code = new_phone_code
        print("Дані про місто  оновлено.")

    def __eq__(self, other):
        return (
                isinstance(other, City) and
                self.name == other.name and
                self.population == other.population

city = City("Київ", "Київський область", "Україна", 3500000, "02095", "+380")

print("Інформація про місто:")
city.display_info()

city.update_data("Берлін", "Брандебург", "Німеччина", "+49", "10115")
city.update_population(3645000)

print("\nОновлена інформація про місто:")
city.display_info()
