# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

print('Введите число и программа выведет это число в обратном порядке.\n', '-' * 20)
num = int(input('Введите число: '))
reverse_num = 0

while num > 0:
    digit = num % 10
    num = num // 10
    reverse_num = reverse_num * 10
    reverse_num = reverse_num + digit
print(reverse_num)