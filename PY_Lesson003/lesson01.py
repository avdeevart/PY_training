# сделано через рекурсию!
def my_factorial(n):
    if n == 0:
        return 1
    else:
        return n * my_factorial(n-1)

a = int(input("Введите число: "))
print(my_factorial(a))
