# Реалізуйте клас «Вебсайт».
# Збережіть у класі: назву вебсайту, адресу та опис вебсайту.
# Реалізуйте конструктор та методи класу для введення-виведення даних,
# а також для інших операцій. Використовуйте механізм перевантаження методів.
print("Завдання №5")
class Website:
    websites_list = []

    def __init__(self, name, address, description):
        self.name = name
        self.address = address
        self.description = description
        Website.websites_list.append(self)

    def display_info(self):
        print("Назва вебсайту: ", self.name)
        print("Адреса: ", self.address)
        print("Опис вебсайту: ", self.description)

    def update_description(self, new_description):
        self.description = new_description
        print("Опис вебсайту оновлено.")

    def update_info(self, new_name, new_address, new_description):
        self.name = new_name
        self.address = new_address
        self.description = new_description
        print("Інформацію про вебсайт оновлено.")

    def display_info(self):
        print("Назва вебсайту: ", self.name)
        print("Адреса: ", self.address)
        print("Опис вебсайту: ", self.description)

    def update_description(self, new_description):
        self.description = new_description
        print("Опис вебсайту оновлено.")

    def update_info(self, new_name, new_address, new_description):
        self.name = new_name
        self.address = new_address
        self.description = new_description
        print("Інформацію про вебсайт оновлено.")

    def __str__(self):
        return f"{self.name}, {self.address}, {self.description}"

    def __ne__(self, other):
        return self.description != other.description

    def __lt__(self, other):
        return len(self.name) < len(other.name)

    @classmethod
    def add_website(cls, name, address, description):
        new_website = cls(name, address, description)
        print(f"Додано новий вебсайт: {new_website.name}")

