def process_numbers(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    min_num = min(numbers)
    max_num = max(numbers)
    squares = [n ** 2 for n in numbers]

    return {
        "sum": total,
        "average": round(avg, 2),
        "min": min_num,
        "max": max_num,
        "squares": squares
    }

def main():
    print("🔢 Number Processor")
    raw_input_data = input("Введите числа через запятую: ")

    try:
        numbers = [float(x.strip()) for x in raw_input_data.split(",") if x.strip()]
    except ValueError:
        print("Ошибка: введите только числа, разделённые запятыми.")
        return

    if not numbers:
        print("Ошибка: вы не ввели ни одного числа.")
        return

    results = process_numbers(numbers)

    print("\n Результаты вычислений:")
    print(f"Сумма чисел: {results['sum']}")
    print(f"Среднее значение: {results['average']}")
    print(f"Минимум: {results['min']}")
    print(f"Максимум: {results['max']}")
    print(f"Квадраты чисел: {results['squares']}")

if __name__ == "__main__":
    main()