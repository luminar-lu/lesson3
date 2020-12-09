def division (num1, num2):
    answ = num1/num2
    return answ


number1 = int(input("Введите делимое : "))
number2 = int(input("Введите делитель : "))
if number2 == 0:
    print("Делить на 0 нельзя!")
else:
    print(f' Частное {division(number1,number2)} . ')