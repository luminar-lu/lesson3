def info(name, sur, year, city, mail, phone ):
    print(f'{name} {sur}, {year} года рождения. Город проживания: {city}.Контактные данные: {mail} {phone }.')

name = input("Введите имя : ")
surname = input("Введите фамилию :")
year = input("Введите год рождения :")
city = input("Введите город проживания :")
email = input("Введите адрес электронной почты :")
phone_number = input("Введите номер телефона :")

info(name= name, sur= surname, year= year, mail= email, city= city, phone= phone_number)