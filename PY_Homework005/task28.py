# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    # если один из аргументов равен нулю, то возвращаем второй аргумент
    if a == 0:
        return b
    if b == 0:
        return a
    # прибавляем 1 к обоим аргументам и вызываем функцию с новыми значениями
    return sum(a + 1, b - 1)

print(sum(int(input("Введите первое слогаемое:")),int(input("Введите второе слогаемое:"))))