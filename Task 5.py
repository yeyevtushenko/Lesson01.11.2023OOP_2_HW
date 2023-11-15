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


