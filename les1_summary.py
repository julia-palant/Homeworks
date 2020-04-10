
home_number = 22 # это переменная
'''
Типы данных:
int целое число
float дробь с плавающей точкой
str срока
bool = Faulse / True
None - тип данных "ничто" 
'''

# number = int(2355) # таким образом мы объявляем тип данных
# var_1 = 2
# var_2 = 5
# var_3 = var_1 + var_2
# 5 % 2 #остаток от целочисленного делени
# var_6 = var_1 // var_2 # целочисленное деление
# var_4 = "STR1" # тип строка
# var_5 = "SRT2"
# var7 = var_4 + var_5 #строки склеются

# Запрос на ввод данных
# Условия и логические операторы. Витвления.
# Циклы For и While
name = input('Ваше имя?\n')
print('Привет', name)

while True:
    age = input('Сколько Вам лет?')
    #print(type(age))
    if age.isdigit():
        age = int(age)
        break
    else:
       print("Ошибка ввода, введите только число")


if age >= 18:
    print('Доступ разрешен ко всем разделам')
elif age > 12:
    print('Посмотри боевечки')
else:
        print('Доступ раздешен к мультикам')


# i = 0
# while 1 < 10:
#     print(i)
#     if i == 4
#         break
#     if i ==3
#         i+=2
#         continue #континью продолжает предыдущий код, в данном случае 42 строку
#     i +=1
# else(Все)

# F строки
name = input()
city = input()
ask_str = f'пользователь {name}, проживает в городе: {city:>10}'

