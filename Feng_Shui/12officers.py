def calculate_output(input1, input2):
    animal_values = {
        "Тигр": 1,
        "Кролик": 2,
        "Дракон": 3,
        "Змея": 4,
        "Лошадь": 5,
        "Коза": 6,
        "Обезьяна": 7,
        "Петух": 8,
        "Собака": 9,
        "Свинья": 10,
        "Крыса": 11,
        "Бык": 12
    }

    difference = animal_values[input2] - animal_values[input1]

    if difference == 0:
        output = 1
    elif difference > 0:
        output = difference + 1
    else:
        output = 12 - abs(difference) + 1

    return output

output_values = {
    1: "Установление",
    2: "Удаление",
    3: "Наполнение",
    4: "Баланс",
    5: "Стабильность",
    6: "Удержание",
    7: "Разрушение",
    8: "Опасность",
    9: "Успех",
    10: "Получение",
    11: "Открытие",
    12: "Закрытие"
}

 # Выводит: "Удаление"

# Пример использования
input1 = "Обезьяна"
input2 = "Кролик"
output = calculate_output(input1, input2)

output_value = output_values[output]
print(output,output_value)