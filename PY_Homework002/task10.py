# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2 - перевернуть!
# ==========================================================================================================================
# Выполнил: Артем Анатольевич Авдеев
# --------------------------------------------------------------------------------------------------------------------------
import random

n_moneys = int(input("Введите количество монеток: "))

# Генерация списка: орел(0)-решка(1)
sides = [random.randint(0, 1) for _ in range(n_moneys)]

# Вывод результата рандома. enumerate - для генерации индексов вместе с элементами списка sides 
# это позволяет  выводить номер каждой монетки, начиная с 1, а не с 0.
for i, side in enumerate(sides):
    print(f"Монетка {i+1}: {side}")

# Подсчет суммы решек
res_side = sum(sides)

# Определение минимального значения
minimus = min(res_side, n_moneys - res_side)

print("Количество монеток, которых нужно перевернуть:", minimus)