# Семинар-1: Задача-1
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

from math import *  #подключение математического модуля

norma = int(input("Норатив расстояния в день (км.):"))
fact = int(input("Введите расстояние, которое проехала машина (км.):"))

#result_time = ceil(fact / norma)
result_time = (fact+norma-1) // norma

print("Машине потребуется: ", result_time, " дней")

