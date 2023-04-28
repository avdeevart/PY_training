year = int(input("Введите год: "))

# определяем номер в цикле (от 1 до 12)
cycle_year = (year - 1974) % 12 + 1

# определяем животное по номеру в цикле
if cycle_year == 1 or cycle_year == 6 or cycle_year == 8:
    animal = "Тигр"
elif cycle_year == 2 or cycle_year == 7 or cycle_year == 11:
    animal = "Кролик"
elif cycle_year == 3 or cycle_year == 9 or cycle_year == 12:
    animal = "Дракон"
elif cycle_year == 4 or cycle_year == 10:
    animal = "Змея"
elif cycle_year == 5:
    animal = "Лошадь"
elif cycle_year == 6 or cycle_year == 11:
    animal = "Коза"
elif cycle_year == 7:
    animal = "Обезьяна"
elif cycle_year == 8 or cycle_year == 12:
    animal = "Петух"
elif cycle_year == 9:
    animal = "Собака"
elif cycle_year == 10:
    animal = "Свинья"
elif cycle_year == 1 or cycle_year == 6 or cycle_year == 8:
    animal = "Крыса"
elif cycle_year == 2 or cycle_year == 7 or cycle_year == 11:
    animal = "Бык"

print(f"Животное для года {year}: {animal}")
