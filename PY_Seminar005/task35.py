# Задача №35:Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Введите число для проверки: "))

if is_prime(num):
    print(f"{num} является простым числом")
else:
    print(f"{num} не является простым числом")
