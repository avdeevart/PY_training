# Задача №19. Решение в группах: Дана последовательность из N целых чисел и число - K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

seq = [1, 2, 3, 4, 5]  # исходная последовательность
k = 3  # количество элементов, на которое необходимо сдвинуть

# В этом коде мы используем срезы списка для выполнения циклического сдвига.
# Сначала мы вычисляем остаток от деления k на длину списка seq с помощью оператора %.
# Это позволяет нам сделать k сдвигов, если k меньше длины списка seq, или выполнить k % len(seq) сдвигов, 
# если k больше или равно длине списка seq.
# Затем мы используем два среза списка: первый срез содержит последние k % len(seq) элементов списка, 
# а второй срез содержит все элементы списка, кроме последних k % len(seq) элементов. Мы объединяем эти два среза,
# чтобы получить список, сдвинутый на k элементов вправ

seq = seq[-k % len(seq):] + seq[:-k % len(seq)]

print(seq)  # выводим результат