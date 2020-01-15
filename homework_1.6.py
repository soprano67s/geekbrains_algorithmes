# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('-'*20,
      '\nВведите три разных числа и программа определит какое из них является средним.\n',
      '-'*20)

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
    print(f"Среднее число: {num1}")
else:
    if num2 > num1 and num2 < num3 or num2 < num1 and num2 > num3:
        print(f"Среднее число: {num2}")
    else:
        if num3 > num1 and num3 < num2 or num3 < num1 and num3 > num2:
            print(f"Среднее число: {num3}")


            