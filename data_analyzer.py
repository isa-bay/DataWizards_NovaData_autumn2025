
# Усовершенствованная версия программы заказа фаст-фуда

class FastFoodOrderSystem:
    def __init__(self):
        self.menu = {
            '1': {'name': 'Куриные наггетсы', 'price': 3.50, 'category': 'Основные блюда'},
            '2': {'name': 'Картофель фри', 'price': 2.50, 'category': 'Гарниры'},
            '3': {'name': 'Чизбургер', 'price': 4.00, 'category': 'Основные блюда'},
            '4': {'name': 'Хот-дог', 'price': 3.50, 'category': 'Основные блюда'},
            '5': {'name': 'Салат Цезарь', 'price': 3.75, 'category': 'Салаты'},
            '6': {'name': 'Большой напиток', 'price': 1.75, 'category': 'Напитки'},
            '7': {'name': 'Средний напиток', 'price': 1.50, 'category': 'Напитки'},
            '8': {'name': 'Маленький напиток', 'price': 1.25, 'category': 'Напитки'},
            '9': {'name': 'Милкшейк', 'price': 2.25, 'category': 'Десерты'},
            '10': {'name': 'Сырный соус', 'price': 0.95, 'category': 'Соусы'},
            '11': {'name': 'Кетчуп', 'price': 0.50, 'category': 'Соусы'},
            '12': {'name': 'Мороженое', 'price': 2.00, 'category': 'Десерты'}
        }

        self.order_history = []

    def display_menu(self):
        """Отображает меню с группировкой по категориям"""
        print("\n" + "=" * 50)
        print("           МЕНЮ РЕСТОРАНА БЫСТРОГО ПИТАНИЯ")
        print("=" * 50)

        categories = {}
        for num, item in self.menu.items():
            category = item['category']
            if category not in categories:
                categories[category] = []
            categories[category].append((num, item))

        for category, items in categories.items():
            print(f"\n{category.upper()}:")
            print("-" * 30)
            for num, item in items:
                print(f"{num:>2}. {item['name']:<20} - ${item['price']:>5.2f}")

    def get_order(self):
        """Получает заказ от пользователя"""
        while True:
            order_input = input("\nВведите номера блюд через пробел (или 'выход' для завершения): ").strip()

            if order_input.lower() in ['выход', 'exit', 'quit']:
                return None

            if not order_input:
                print("⚠️  Пожалуйста, введите номера блюд!")
                continue

            return order_input.split()

    def process_order(self, order_items):
        """Обрабатывает заказ и возвращает результат"""
        if not order_items:
            return None

        order_details = {}
        total = 0
        invalid_items = []

        for item_num in order_items:
            if item_num in self.menu:
                item = self.menu[item_num]
                item_name = item['name']
                order_details[item_name] = order_details.get(item_name, 0) + 1
                total += item['price']
            else:
                invalid_items.append(item_num)

        return {
            'items': order_details,
            'total': total,
            'invalid_items': invalid_items
        }

    def display_order_summary(self, order_result):
        """Отображает сводку заказа"""
        if not order_result or not order_result['items']:
            print("❌ Заказ пуст!")
            return

        print("\n" + "=" * 40)
        print("          СВОДКА ЗАКАЗА")
        print("=" * 40)

        for item, count in order_result['items'].items():
            price = next(menu_item['price'] for menu_item in self.menu.values()
                         if menu_item['name'] == item)
            print(f"  {count:>2}x {item:<20} ${price * count:>6.2f}")

        print("-" * 40)
        print(f"  ИТОГО: ${order_result['total']:>24.2f}")
        print("=" * 40)

        if order_result['invalid_items']:
            print(f"\n⚠️  Не найдены в меню: {', '.join(order_result['invalid_items'])}")

    def apply_discount(self, total):
        """Применяет скидку в зависимости от суммы заказа"""
        discount = 0
        if total > 20:
            discount = 0.15  # 15% скидка
            print("🎉 Скидка 15% применена (заказ свыше $20)!")
        elif total > 15:
            discount = 0.10  # 10% скидка
            print("🎉 Скидка 10% применена (заказ свыше $15)!")
        elif total > 10:
            discount = 0.05  # 5% скидка
            print("🎉 Скидка 5% применена (заказ свыше $10)!")

        discount_amount = total * discount
        final_total = total - discount_amount

        if discount > 0:
            print(f"  Сумма скидки: ${discount_amount:>19.2f}")
            print(f"  К ОПЛАТЕ: ${final_total:>22.2f}")

        return final_total

    def save_order_to_history(self, order_result, final_total):
        """Сохраняет заказ в историю"""
        if order_result and order_result['items']:
            self.order_history.append({
                'items': order_result['items'].copy(),
                'subtotal': order_result['total'],
                'final_total': final_total,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    def display_order_history(self):
        """Отображает историю заказов"""
        if not self.order_history:
            print("\n📝 История заказов пуста")
            return

        print("\n" + "=" * 50)
        print("           ИСТОРИЯ ЗАКАЗОВ")
        print("=" * 50)

        for i, order in enumerate(self.order_history, 1):
            print(f"\nЗаказ #{i} ({order['timestamp']}):")
            for item, count in order['items'].items():
                print(f"  {count}x {item}")
            print(f"  Итого: ${order['final_total']:.2f}")

    def run(self):
        """Основной цикл программы"""
        print("Добро пожаловать в систему заказов!")
        print("Для завершения работы введите 'выход'")

        while True:
            self.display_menu()
            order_items = self.get_order()

            if order_items is None:
                break

            order_result = self.process_order(order_items)

            if order_result and order_result['items']:
                self.display_order_summary(order_result)
                final_total = self.apply_discount(order_result['total'])
                self.save_order_to_history(order_result, final_total)

                # Подтверждение заказа
                confirm = input("\nПодтвердить заказ? (да/нет): ").strip().lower()
                if confirm in ['да', 'yes', 'y', 'д']:
                    print("✅ Заказ подтвержден! Приятного аппетита! 🍔")
                else:
                    print("❌ Заказ отменен")
            else:
                print("❌ Не удалось обработать заказ. Попробуйте снова.")

        # Показываем историю заказов при выходе
        self.display_order_history()
        print("\nСпасибо за использование нашей системы! До свидания! 👋")


# Запуск программы
if __name__ == "__main__":
    import datetime

    system = FastFoodOrderSystem()
    system.run()
