# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

print('Программа определяет сколько чисел от 2 до 99, кратны числам от 2 до 9.\n', '-' * 20)

begin = 2
finish = 9
min_num = 2
max_num = 99
count = 0

for i in range(begin, finish + 1):
    for x in range(min_num, max_num + 1):
        if x % i == 0:
            count += 1
    print(f'{i} кратно {count} числам')
