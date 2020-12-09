arr_1 = []
# доп задание
name_arr = []
valume_arr = []
unit_arr = []
price_arr = []
#
count = 1
while True:
    name = input("Введите название товара. Если товаров больше нет введите 0 : ")
    if name == "0":
        break
    else:
        price = input("Введите цену :")
        volume = input("Введите количество :")
        unit = input("Введите единицу измерения :")
        article = {"name":name, "price":price, "volume":volume, "unit":unit, "number":count}
        arr_1.append(article)
        count = count + 1
        #   доп задание
        name_arr.append(name)
        valume_arr.append(volume)
        price_arr.append(price)
        unit_arr.append(unit)
        #
for i in range(len(arr_1)):
    print(f'{arr_1[i]["number"]}) Название:{arr_1[i]["name"]}, цена {arr_1[i]["price"]}, количество {arr_1[i]["volume"]} {arr_1[i]["unit"]}.')
# доп задание
revision={"name":name_arr,"valume":valume_arr,"price":price_arr, "unit":unit_arr}



