# передача функции неограниченного количества аргументов - ставим *args
def sum_str(*args):
    res = ""
    for i in args:
        if isinstance(i, str):
            res += i
        else:
            res += str(i)
    return res

print(sum_str("c","e","f","g","h"))

print(sum_str(1,2,3,4,5,6,7,8,9,10,11,12,13))

