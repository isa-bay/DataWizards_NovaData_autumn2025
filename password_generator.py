import random
import string

def generate_password(length=12):
    """
    Генерирует случайный пароль заданной длины
    """
    # Все возможные символы для пароля
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Пример использования
if __name__ == "__main__":
    password_length = int(input("Введите длину пароля: ") or 12)
    password = generate_password(password_length)
    print(f"Сгенерированный пароль: {password}")