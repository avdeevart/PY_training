# Функция для вычисления даты нового года по китайскому календарю
def chinese_new_year(year):
    c_year = (year - 3) % 60 % 12 + 1-3
    print(c_year)
    
    # Вычисляем дату нового года в формате (месяц, день)
    # Формула взята из https://en.wikipedia.org/wiki/Chinese_New_Year
    if c_year == 1:
        date = (2, 1)
    elif c_year == 2:
        date = (1, 22)
    elif c_year == 3:
        date = (2, 10)
    elif c_year == 4:
        date = (1, 29)
    elif c_year == 5:
        date = (2, 17)
    elif c_year == 6:
        date = (2, 6)
    elif c_year == 7:
        date = (1, 26)
    elif c_year == 8:
        date = (2, 13)
    elif c_year == 9:
        date = (2, 3)
    elif c_year == 10:
        date = (1, 23)
    elif c_year == 11:
        date = (2, 11)
    else:
        date = (1, 31)
    
    return date

# Вводим год с консоли
year = int(input("Введите год: "))

# Вычисляем дату нового года по китайскому календарю
date = chinese_new_year(year)

# Выводим результат на консоль
print("Новый год по китайскому календарю в год", year, "будет", date[1], "числа", date[0], "месяца")
