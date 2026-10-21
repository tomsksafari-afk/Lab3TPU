products = ["Клавиатура", "Мышь", "Монитор", "Кабель"]
amounts = [12, 4, 7, 25]

# Формируем словарь остатков
stock = dict(zip(products, amounts))
print(stock)

# Находим товары, которые нужно заказать
to_order = [product for product, amount in stock.items() if amount < 10]
print(to_order)