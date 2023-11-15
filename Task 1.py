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

    def __eq__(self, other):
        return isinstance(other, Person) and self.full_name == other.full_name and self.date_of_birth == other.date_of_birth

    def __lt__(self, other):
        return self.date_of_birth < other.date_of_birth


person1 = Person("Олексій", "06.12.2006", "+380765870090", "Київ", "Україна", "вул. Академіка Янгеля 16/2")
person2 = Person("Ірина", "15.05.1990", "+380987654321", "Львів", "Україна", "вул. Шевченка, 5")

print("Чи рівні особи:")
print(person1 == person2)

print("\nПорівняння осіб за датою народження:")
print(person1 < person2)
