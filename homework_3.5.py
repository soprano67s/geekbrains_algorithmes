# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

massive = [random.randint(-20, 20) for i in range(10)]
print(massive)
count = -1
i = 0

for i in range(len(massive)):
    if massive[i] < 0 and count == -1:
        count = i
    elif 0 > massive[i] > massive[count]:
        count = i
    i += 1

if count != -1:
    print(f'Максимальное отрицательное число: {massive[count]} '
          f'Номер в массиве: {count}')



