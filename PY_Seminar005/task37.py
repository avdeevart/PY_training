# Задача №37:Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def print_reverse_sequence(n):
    if n == 0:
        return
    element = int(input("ввод:"))
    print_reverse_sequence(n-1)
    print("реверс:",element)

n = int(input("Введите число N:"))
print_reverse_sequence(n)
