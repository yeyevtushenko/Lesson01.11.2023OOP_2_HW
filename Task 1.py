"""До вже реалізованого класу «Людина» додайте конструктор та необхідні перевантажені методи."""
print("Завдання №1")
# З попереднього домашнього завдання візьмемо візьмемо готовий реалізований клас
class Person:
    def __init__(self, full_name, date_of_birth, phone_number, city, country, adress):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.adress = adress

    def display_info(self):
        print("ПІБ: ", self.full_name)
        print("Дата народження: ", self.date_of_birth)
        print("Контактний телефон: ", self.phone_number)
        print("Місто: ", self.city)
        print("Країна: ", self.country)
        print("Домашня адреса: ", self.adress)

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        print("Контактний телефон оновлено.")

    def update_adress(self, new_city, new_country, new_address):
        self.cit = new_city
        self.country = new_country
        self.adress = new_address
        print("Адресу проживання оновлено.")

    def __str__(self):
        return f"{self.full_name}, {self.date_of_birth}, {self.phone_number}, {self.city}, {self.country}, {self.address}"

person = Person("Олексій", "06.12.2006", "+380765870090", "Киів", "Україна", "вул. Академіка Янгеля 16/2")

print("Інформація про людину:")
person.display_info()

person.update_phone_number("+987654321")

person.update_adress("Львів", "Україна", "вул. Шевченка, 5")
print("\nОновлена інформація про людину:")
person.display_info()
