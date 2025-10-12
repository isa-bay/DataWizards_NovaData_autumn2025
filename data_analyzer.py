menu = {
    '1': ('Куриные наггетсы', 3.50),
    '2': ('Картофель фри', 2.50),
    '3': ('Чизбургер', 4.00),
    '4': ('Хот-дог', 3.50),
    '5': ('Салат', 3.75),
    '6': ('Большой напиток', 1.75),
    '7': ('Средний напиток', 1.50),
    '8': ('Маленький напиток', 1.25),
    '9': ('Милкшейк', 2.25),
    '10': ('Сырный соус', 0.95)
}

while True:
    print("\nМеню:")
    for k, (item, price) in menu.items():
        print(f"{k}. {item} - ${price:.2f}")

    order = input("\nВведите номера заказа: ")
    if not order:
        break

    items = {}
    total = 0
    for num in order:
        if num in menu:
            item, price = menu[num]
            items[item] = items.get(item, 0) + 1
            total += price

    print("\nСводка заказа:")
    for item, count in items.items():
        print(f"{count}x {item}")
    print(f"Итого: ${total:.2f}")