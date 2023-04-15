# Задаем список возможных значений "небесного ствола" и "земной ветви"
heavenly_stems = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
earthly_branches = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# Запрашиваем у пользователя год рождения в григорианском календаре
year = int(input("Введите год рождения в григорианском календаре: "))

# Вычисляем значение "небесного ствола" и "земной ветви" по заданным формулам
heavenly_stem = heavenly_stems[(year - 4) % 10]
earthly_branch = earthly_branches[(year - 4) % 12]

# Выводим результат
print("Ваш год рождения по китайскому календарю: {}{}".format(heavenly_stem, earthly_branch))

# ----------------------------------------------------------------------------------------------------------------
def calculate_heavenly_stem_day(date):
    day, month, year = map(int, date.split('.'))
    heavenly_stem = (year % 10) % 5
    earthly_branch = (year % 12) - 3
    day_heavenly_stem = (day + earthly_branch + 1) % 10
    return heavenly_stem, day_heavenly_stem

print(calculate_heavenly_stem_day("{0}.{1}.{2}".format(30, 12, 1975)))
