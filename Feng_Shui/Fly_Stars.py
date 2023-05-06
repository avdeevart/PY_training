# Создаем словарь соответствия элементов и номеров
elements = {
    0: "металл",
    1: "вода",
    2: "дерево",
    3: "огонь",
    4: "земля"
}

def calculate_flying_stars(year, animal_sign):
    # Определяем элемент на основе номера знака животного
    element = animal_sign % 5
    element_name = elements[element]

    # Расчет часовой звезды
    hour_star = (4 - element) % 9 + 1

    # Расчет дневной звезды
    day_star = (10 - element) % 9 + 1

    # Расчет месячной звезды
    month_star = (7 - element) % 9 + 1

    # Расчет годовой звезды
    year_star = (year - 4) % 9 + 1

    # Расчет звезды 20-летия
    twenty_year_star = ((year // 20 + year % 20) % 9) + 1

    # Возвращаем словарь с летящими звездами
    return {
        "Часовая": hour_star,
        "Дневная": day_star,
        "Месячная": month_star,
        "Годовая": year_star,
        "20-летняя": twenty_year_star
    }

# Запрашиваем у пользователя данные
try:
    year = int(input("Введите год рождения: "))
    animal_sign = int(input("Введите номер знака животного: "))
    if not 1 <= animal_sign <= 12:
        raise ValueError("Номер знака животного должен быть от 1 до 12.")
except ValueError as error:
    print(f"Ошибка: {error}")
else:
    # Вызываем функцию и выводим результат
    flying_stars = calculate_flying_stars(year, animal_sign)
    print(f"Летящие звезды для года {year} и знака животного номер {animal_sign}:")
    for star, number in flying_stars.items():
        print(f"{star}: {number}")

# Крыса-1
# Бык-2
# Тигр
# Кролик-4
# Дракон
# Змея
# Лошадь
# Овца (Козел)
# Обезьяна
# Петух
# Собака
# Свинья-12