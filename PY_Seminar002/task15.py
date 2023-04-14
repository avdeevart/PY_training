# Задача №15: Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:арбузов слишком много
# и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно число N
# – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

number_of_watermelons=int(input("Введите количество арбузов: "))
maxi_watermelon_weight=0
mini_watermelon_weight=0
# Цикл генерирования веса арбуза
for watermelon in range(number_of_watermelons):
    # Генерация случайной веса арбуза
    watermelon_weight = random.randint(1, 50)

    # Вывод сгенерированной веса
    print(f"Вес арбуза {watermelon+1}: {watermelon_weight} кг.")

    # Поиск максимального и минимального веса арбузов
    if watermelon_weight>maxi_watermelon_weight:
        maxi_watermelon_weight=watermelon_weight
    else:
        mini_watermelon_weight=watermelon_weight
print("Для себя арбуз весом -",maxi_watermelon_weight,"кг., а для тещи весом -",mini_watermelon_weight,"кг.")
