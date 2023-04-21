# Задача №33: Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# ----------------------------------------------------------------------------------------------------------------------------
import random

length = int(input("Введите количество оценок Васи: "))

# Используем генератор списка для создания списка со случайными числами
actual_evaluation = [random.randint(1, 5) for i in range(length)]

print("Вася получил следующие оценки:", actual_evaluation)

# Поиск максимального значения
max_value = max(actual_evaluation)
print("Максимальное значение:", max_value)

# Поиск минимального значения
min_value = min(actual_evaluation)
print("Минимальное значение:", min_value)

# Замена всех максимальных значений минимальным значением
max_indices = [i for i, x in enumerate(actual_evaluation) if x == max_value]
for index in max_indices:
    actual_evaluation[index] = min_value

print("Измененный список оценок Васи:", actual_evaluation)

