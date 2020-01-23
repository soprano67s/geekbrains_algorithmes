# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

begin = 32
finish = 127
x = ''
i = 0

def recursion(a, b, c, i):
    if a == b:
        c += f'{a}: {chr(a)} '
        return c
    else:
        c += f'{a}: {chr(a)} \t'
        i += 1
        if i == 10:
            c += '\n'
            i = 0
        return recursion(a + 1, b, c, i)

result = recursion(begin, finish, x, i)
print(result)