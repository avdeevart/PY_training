year = int(input("Введите год: "))
month = int(input("Введите номер месяца: "))

reference_date = (1975, 12, "Ян", "земля")
heavenly_stems = [("Ян", "земля"), ("Инь", "земля"), ("Ян", "металл"), ("Инь", "металл"), ("Ян", "вода"), ("Инь", "вода"), ("Ян", "дерево"), ("Инь", "дерево"), ("Ян", "огонь"), ("Инь", "огонь")]

# вычисляем порядковый номер месяца относительно опорной даты
months_since_reference = (year - reference_date[0]) * 12 + (month - reference_date[1])

# вычисляем индекс небесного ствола для данного месяца
heavenly_stem_index = months_since_reference % 10

# получаем название небесного ствола из списка
heavenly_stem = heavenly_stems[heavenly_stem_index]

print("Небесный ствол для {}-го месяца {} года: {} ({})".format(month, year, heavenly_stem[0], heavenly_stem[1]))
