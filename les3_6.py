def int_func(arr,i):
    str_2 = (arr[i]).capitalize()
    return str_2
a = str()

str_1 = input("Введите строку :")
arr_1 = str_1.split()
for i in range(len(arr_1)):
    a = a + " " + int_func(arr_1,i)
print(a)