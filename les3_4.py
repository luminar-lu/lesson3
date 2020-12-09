def my_func_1(x,y):
    answ = x
    for a in range(y-1):
        answ = answ * x
        a = a + 1
    return answ

def my_func_2(x,y):
    answ = x ** y
    return answ

print(my_func_1(2, 8))
print(my_func_2(4, 4))
