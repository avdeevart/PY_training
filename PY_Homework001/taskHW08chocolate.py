# Домашнее задание№8/Семинар№1:
# ========================================================================================================
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками, то есть разломить шоколадку на два прямоугольника. 3 2 4 -> yes / 3 2 1 -> no
# =========================================================================================================
# Решил: Артем Анатольевич Авдеев
# ________________________________________________________________________________________________________

print("Задайте габаритные размеры шоколадки в дольках:")
n = int(input("Количество долек по горизонтали: "))
m = int(input("Количество долек по вертикали: "))

print("Размер вашей шоколадки:", n, "x", m, "Всего долек в шоколадке:", n * m)

k = int(input("Введите количество долек, которые хотите отломить за один раз: "))

# Наш Гений решил создать функцию, возращающую булевское значение "истина" при выпонении условий задачи
# Да, мы функции не проходили. Однако, я почитал про них + имею опыт кодинга на сях,паскалях и байсиках :)

def broken_chocolate(n, m, k):
    if k == 1:
        return False
    elif k > n * m:
        return False
    elif k % n == 0 or k % m == 0:
        return True
    else:
        return False

# Вызываем функцию broken_chocolate и передаем ей аргументы n, m, k
if broken_chocolate(n, m, k):
    print("Вы можете правильно сломать шоколадку")
else:
    print("Вот облом! Шоколадку правильно не сломаешь!")