def chinese_new_year(year):
    # Определяем номер года по китайскому календарю
    c_year = (year - 3) % 60 % 12 + 1-3
    
    # Определяем дату нового года по китайскому календарю
    date_dict = {
        1: (2, 1),
        2: (1, 22),
        3: (2, 10),
        4: (1, 29),
        5: (2, 17),
        6: (2, 6),
        7: (1, 26),
        8: (2, 13),
        9: (2, 3),
        10: (1, 23),
        11: (2, 11),
        12: (1, 31)
    }
    date = date_dict[c_year]
    
    return date

# Вводим год с консоли
year = int(input("Введите год: "))

# Вычисляем дату нового года по китайскому календарю
date = chinese_new_year(year)

# Выводим результат на консоль
print("Новый год по китайскому календарю в год", year, "будет", date[1], "числа", date[0], "месяца")