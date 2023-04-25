# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# input: 7 2 5
# output: 7 9 11 13 15

a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов в прогрессии: "))

arr = [str(a1 + (i-1)*d) for i in range(1, n+1)]
print(" ".join(arr))
