# Определить, какое число в массиве встречается чаще всего
import random



massive = [random.randint(10, 20) for i in range(20)]
print(massive)
first_count = 1

for i in range(len(massive)):
    second_count = 1
    for x in range(i + 1, len(massive)):
        if massive[i] == massive[x]:
            second_count += 1
    if second_count > first_count:
        first_count = second_count
        result = massive[i]


if first_count > 1:
    print(f'Число встречающееся чаще всех: {result} \n'
          f'Сколько раз: {first_count}')
else:
    print('Нет повторяющихся чисел.')