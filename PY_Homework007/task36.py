# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения. Начинать с 1!
# print_operation_table(lambda x, y: x * y)

def print_operation_table(operation, num_rows=6, num_columns=6):
    # Генерируем список заголовков столбцов и выравниваем их по правому краю каждого столбца
    column_headers = [f"{column:>4d}" for column in range(1, num_columns + 1)]

    # Печатаем заголовок таблицы
    print("    ", *column_headers)

    # Печатаем разделительную линию
    print("   +" + "-" * (5 * num_columns))

    # Печатаем содержимое таблицы
    for row in range(1, num_rows + 1):
        # Генерируем список значений для текущей строки
        row_values = [operation(row, column) for column in range(1, num_columns + 1)]

        # Преобразуем значения в строки и печатаем текущую строку
        print(f"{row:2d} |", *map(lambda value: f"{value:4d}", row_values))

# Функция для умножения двух чисел
multiply = lambda x, y: x * y

# Вывод таблицы умножения
print_operation_table(multiply)
