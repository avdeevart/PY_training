# Задача №11. Решение в группах:Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

inp_digit=int(input("Введите целое, положительное число: "))

def fib_index(A):
    # Начальные значения чисел Фибоначчи
    fib_n_2, fib_n_1 = 0, 1
    # Первое число Фибоначчи имеет индекс 1
    index = 2
    # Пока текущее число Фибоначчи меньше или равно A
    while fib_n_1 <= A:
        # Если текущее число Фибоначчи равно A, то возвращаем его индекс
        if fib_n_1 == A:
            return index
        # Иначе переходим к следующему числу Фибоначчи
        fib_n_2, fib_n_1 = fib_n_1, fib_n_1 + fib_n_2
        index += 1
    # Если A не является числом Фибоначчи, возвращаем -1
    return -1

print(fib_index(inp_digit))
