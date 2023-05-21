# Задача №51:Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
# Ввод:
# values = [0, 2, 10, 6]
# Вывод: same

# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, objects):
    # Создаем множество для хранения уникальных значений характеристики
    unique_values = set(characteristic(obj) for obj in objects)
    
    # Если множество содержит только одно значение, значит все объекты имеют одинаковую характеристику
    return len(unique_values) == 1

values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

