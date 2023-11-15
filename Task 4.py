# Реалізуйте клас «Годинник».
# Збережіть у класі: назву моделі годинника, виробника годинника, р
# ік випуску, ціну годинника, тип годинника (наручний, настінний і т. д.).
# Реалізуйте конструктор та методи класу для введення-виведення даних, а також для інших операцій.
# Використовуйте механізм перевантаження методів.
print("Завдання №4")
class Watch:
    def __init__(self, model, manufacturer, year, price, watch_type):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def display_info(self):
        print("Модель годинника: ", self.model)
        print("Виробник: ", self.manufacturer)
        print("Рік випуску: ", self.year)
        print("Ціна: ", self.price)
        print("Тип годинника: ", self.watch_type)

    def update_price(self, new_price):
        self.price = new_price
        print("Ціна годинника оновлена.")

    def update_info(self, new_model, new_manufacturer, new_year, new_watch_type):
        self.model = new_model
        self.manufacturer = new_manufacturer
        self.year = new_year
        self.watch_type = new_watch_type
        print("Інформацію про годинник оновлено.")

    def __str__(self):
        return f"{self.model}, {self.manufacturer}, {self.year}, {self.price}, {self.watch_type}"

    def __eq__(self, other):
        return (
                isinstance(other, Watch) and
                self.model == other.model and
                self.manufacturer == other.manufacturer
        )