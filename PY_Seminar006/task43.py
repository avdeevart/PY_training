# Задача №43: Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. 
# Все числа списка находятся на разных строках.

# import random

# length = int(input("Введите длину списка: "))
# array = [random.randint(0, 10) for _ in range(length)]
# print("Сгенерированный список:", array)

# count = sum(n*(n-1)//2 for n in [array.count(i) for i in set(array)])

# print("Количество пар элементов, равных друг другу:", count)

def count_pairs(lst):
    if len(lst) < 2:
        return 0
    else:
        first = lst[0]
        rest = lst[1:]
        count = rest.count(first)
        return count + count_pairs(rest)

import random

length = int(input("Введите длину списка: "))
lst = [random.randint(0, 10) for _ in range(length)]
print("Сгенерированный список:", lst)
count = count_pairs(lst)
print(count)
