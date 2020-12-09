def my_func(a, b, c):
    answ = a + b + c - min(a,b,c)
    return answ
number1 = int(input("Введите первое число :"))
number2 = int(input("Введите второе число :"))
number3 = int(input("Введите третье число :"))
print(f' Сумма двух больших чисел равна {my_func(number1, number2, number3)}.')