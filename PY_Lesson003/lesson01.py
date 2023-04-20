def my_factorial(n):
    summa=1
    for i in range(1,n+1):
        summa *=i
    return summa
a =int(input("Введите число:"))
print(my_factorial(a))        