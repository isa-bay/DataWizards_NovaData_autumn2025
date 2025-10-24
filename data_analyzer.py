# Разработчик: Байрамов Иса
# Программа заказа фаст-фуда - ВЕРСИЯ СО СКИДКАМИ

menu = {
    '1': ('Куриные наггетсы', 3.50),
    '2': ('Картофель фри', 2.50),
    '3': ('Чизбургер', 4.00),
    '4': ('Хот-дог', 3.50),
    '5': ('Салат Греческий', 4.25),
    '6': ('Большой напиток', 1.75),
    '7': ('Средний напиток', 1.50),
    '8': ('Маленький напиток', 1.25),
    '9': ('Милкшейк', 2.25),
    '10': ('Сырный соус', 0.95),
    '11': ('Кофе латте', 2.50)
}


def apply_discount(subtotal, item_count):
    """Применяет скидки к заказу"""
    discount = 0

    if subtotal > 20:
        discount = subtotal * 0.15  # 15% скидка
        print(f"Скидка 15%: -${discount:.2f}")
    elif subtotal > 15:
        discount = subtotal * 0.10  # 10% скидка
        print(f"Скидка 10%: -${discount:.2f}")
    elif item_count >= 3:
        discount = subtotal * 0.05  # 5% скидка
        print(f"Скидка на 3+ товара: -${discount:.2f}")

    return discount


while True:
    print("\n" + "=" * 45)
    print("    ДОБРО ПОЖАЛОВАТЬ В НАШ РЕСТОРАН!")
    print("=" * 45)
    print("АКЦИЯ: Заказ от $20 - скидка 15%!")

    for k, (item, price) in menu.items():
        print(f"{k}. {item:<20} ${price:>5.2f}")

    order = input("\nВведите номера блюд (через пробел): ")
    if order.lower() in ['выход', 'exit', '']:
        print("До свидания! Ждем снова!")
        break

    items = {}
    invalid_items = []
    total_items = 0

    for num in order.split():
        if num in menu:
            item, price = menu[num]
            items[item] = items.get(item, 0) + 1
            total_items += 1
        else:
            invalid_items.append(num)

    if not items:
        print("Ошибка: В заказе нет действительных позиций!")
        continue

    print("\n" + "=" * 45)
    print("          ВАШ ЗАКАЗ")
    print("=" * 45)

    subtotal = 0
    for item, count in items.items():
        price = next(price for name, price in menu.values() if name == item)
        item_total = price * count
        subtotal += item_total
        print(f"  {count}x {item:<20} ${item_total:>6.2f}")

    discount = apply_discount(subtotal, total_items)
    final_total = subtotal - discount

    print(f"\n  Подытог: ${subtotal:>26.2f}")
    if discount > 0:
        print(f"  Скидка: -${discount:>25.2f}")
    print(f"  ИТОГО: ${final_total:>27.2f}")

    if invalid_items:
        print(f"\n  Внимание: Неизвестные позиции - {', '.join(invalid_items)}")

    print("=" * 45)

    # Подтверждение заказа
    confirm = input("\nПодтвердить заказ? (да/нет): ").lower()
    if confirm in ['да', 'yes', 'y']:
        print("✅ Заказ принят! Приятного аппетита!")
    else:
        print("❌ Заказ отменен")