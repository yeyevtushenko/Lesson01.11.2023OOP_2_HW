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