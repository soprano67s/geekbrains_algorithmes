# https://drive.google.com/file/d/1VK_XMXAsNoj3wUwnpo04JtzoRuXjnX7F/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите трёхзначное число и программа посчитает сумму и произведение данных чисел: '))

if len(str(x)) == 3:
    sum1 = int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2])
    sum2 = int(str(x)[0]) * int(str(x)[1]) * int(str(x)[2])
    print(f"Сумма цифр введённого числа: {sum1}")
    print(f"Произведение цифр введённого числа: {sum2}")
else:
    print('Ошибка. Введенное число неверного формата.\n(Число должно состоять из 3 цифр)')
