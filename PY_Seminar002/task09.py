# Задача №9. Решение в группах: По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
input_num = int(input("Введите целое, неотрицательное число: "))

if input_num < 0:
    print("Ошибка: введено отрицательное число")
else:
    fctrl_num = 1
    i = 1
    while i <= input_num:
        fctrl_num *= i
        i += 1
    print("Факториал числа", input_num, "!=", fctrl_num)