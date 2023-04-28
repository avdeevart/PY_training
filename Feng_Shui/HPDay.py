from datetime import date

BASE_TABLE = [
    ('Ян', 'металл'),
    ('Инь', 'металл'),
    ('Ян', 'вода'),
    ('Инь', 'вода'),
    ('Ян', 'дерево'),
    ('Инь', 'дерево'),
    ('Ян', 'огонь'),
    ('Инь', 'огонь'),
    ('Ян', 'земля'),
    ('Инь', 'земля')
]

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

input_date = date(year, month, day)
base_date = date(1975, 12, 30)

delta_days = (input_date - base_date).days
heavenly_stem, sign = BASE_TABLE[delta_days % 10]

print(f"Небесный ствол дня: {heavenly_stem}, знак: {sign}")
