# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

massive = []
min_ = 0
max_ = 0

for i in range(10):
    massive.append(random.randint(-100, 100))

print(massive,'\n','-'*40)

for i in range(len(massive)):
    if massive[i] < massive[min_]:
        min_ = i
    elif massive[i] > massive[max_]:
        max_ = i

massive[min_], massive[max_] = massive[max_], massive[min_]
print(massive)
