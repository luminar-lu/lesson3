# я не понял как это нужно реализовать, поэтому сделал очень криво, извините
summ = 0
a = [0, 0]
arr_1 = []
def summ_f(arr_1, summ):
    for i in range(len(arr_1)):
        if arr_1[i] == "q":
            a[0] = 1
        else:
            summ = summ + int(arr_1[i])
            a[1] = summ
    return a

while True:
    str_1 = input("Введите числа через пробел. Для остановки введите q : ")
    arr_1 = str_1.split(" ")
    summ = a[1]
    a = summ_f(arr_1,summ)
    if a[0] == 1:
        print(f'Cумма введенных чисел: {a[1]}')
        break
    else:
        print(f'Cумма введенных чисел: {a[1]}')


