# Тема модули! Главный файл, в который будем импортировать модули.add()

# # Вариант 1 - импорт на прямую из файла
# # указываем из какого файла импортируем функцию
# import lesson03
# # вызываем импортируемую функцию
# print(lesson03.max1(5,9))


# Вариант 2 - здесь на прямую импортируем функцию
from lesson03 import max1
print(max1(9,5))

# Вариант 3 - если не хотим отдельно перечислят все импортируемые модули из файла, то:
from lesson03 import *

# Вариант 4 - импортировать модуль lesson03 как "псевдоним" (например: m1)
import lesson03 as m1
print(m1.max1(9,5))
