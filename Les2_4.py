str_1 = input("Введите строчку :")
index=1
str_2=str_1.split(" ")
for i in range((len(str_2))):
        print(f'{i+1}) {str_2[i][0:10]}.')


