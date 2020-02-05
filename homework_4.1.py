# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

import cProfile
import timeit


# ВЫВОД:
# 1. Первый алгоритм(рекурсия) оказался самым медленым. Но если n < 100, то алгоритм будет быстрее всех.
#       -При увеличении n в 10 раз, время увеличивается примерно в 100 раз

# 2. Второй алгоритм отработал быстрее всех.
#       -При увеличении n в 10 раз, время увеличивается примерно в 4 раза

# 3. Третий алгоритм оказался средним по быстроте, но не на много медленее второго, но в разы быстрее первого.
#       -При увеличении n в 10 раз, время увеличивается примерно в 10 раз




# ==========  1 вариант  ==========

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

print('-'*82, '\n', '-'*80)


# print(timeit.timeit('recursion(begin, 100, x, i)', number=100, globals=globals()))          #   0.0054726350000000035
# print(timeit.timeit('recursion(begin, 250, x, i)', number=100, globals=globals()))          #   0.028971379999999998
# print(timeit.timeit('recursion(begin, 500, x, i)', number=100, globals=globals()))          #   0.125955943
# print(timeit.timeit('recursion(begin, 1000, x, i)', number=100, globals=globals()))         #   0.606736078

# ---------------------------------------------
# cProfile.run('recursion(begin, finish, x, i)')
# ---------------------------------------------
#     195 function calls (100 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      96/1    0.000    0.000    0.000    0.000 homework_4.1.py:13(recursion)
#        96    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('recursion(begin, 250, x, i)')
# ---------------------------------------------
#     441 function calls (223 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     219/1    0.000    0.000    0.000    0.000 homework_4.1.py:13(recursion)
#       219    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('recursion(begin, 500, x, i)')
# ---------------------------------------------
#     941 function calls (473 primitive calls) in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#     469/1    0.002    0.000    0.003    0.003 homework_4.1.py:13(recursion)
#       469    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('recursion(begin, 1000, x, i)')
# ---------------------------------------------
#     1941 function calls (973 primitive calls) in 0.016 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#     969/1    0.016    0.000    0.016    0.016 homework_4.1.py:13(recursion)
#       969    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------




# ==========  2 вариант  ==========

count = 0
def test_2(begin, finish, x, count):
    for i in range(begin, finish + 1):
        if i != finish + 1:
            x += f'{i}: {chr(i)} \t'
            count += 1
        if count == 10:
            x += '\n'
            count = 0
    return x

print(test_2(begin, finish, x, count))
print('-'*82, '\n', '-'*80)

# print(timeit.timeit('test_2(begin, 100, x, count)', number=100, globals=globals()))         #   0.016302305000000003
# print(timeit.timeit('test_2(begin, 250, x, count)', number=100, globals=globals()))         #   0.013992471
# print(timeit.timeit('test_2(begin, 500, x, count)', number=100, globals=globals()))         #   0.03723084
# print(timeit.timeit('test_2(begin, 1000, x, count)', number=100, globals=globals()))        #   0.06678970700000002


# ---------------------------------------------
# cProfile.run('test_2(begin, finish, x, count)')
# ---------------------------------------------
# 100 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 homework_4.1.py:99(test_2)
#        96    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ----------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('test_2(begin, 250, x, count)')
# ---------------------------------------------
# 223 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 homework_4.1.py:99(test_2)
#       219    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ----------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('test_2(begin, 500, x, count)')
# ---------------------------------------------
# 473 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 homework_4.1.py:99(test_2)
#       469    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ----------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('test_2(begin, 1000, x, count)')
# ---------------------------------------------
# 973 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 homework_4.1.py:99(test_2)
#       969    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ----------------------------------------------------------------------------------------------




# ==========  2 вариант  ==========




row = ''
result = ''

def test_3(begin, finish, row, result):
    for i in range(begin, finish + 1):
        row += '{}:{}\t'.format(i, chr(i))
        if not (i - 31) % 10:
            result += '{}\n'.format(row)
            row = ''
    result += '{}\n'.format(row)
    return result

print(test_3(begin, finish, row, result))
# print(timeit.timeit('test_3(begin, 100, row, result)', number=100, globals=globals()))      #   0.008339687999999998
# print(timeit.timeit('test_3(begin, 250, row, result)', number=100, globals=globals()))      #   0.017143602999999993
# print(timeit.timeit('test_3(begin, 500, row, result)', number=100, globals=globals()))      #   0.037699444
# print(timeit.timeit('test_3(begin, 1000, row, result)', number=100, globals=globals()))     #   0.08613629500000002


# ---------------------------------------------
# cProfile.run('test_3(begin, 100, row, result)')
# ---------------------------------------------
# 149 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 homework_4.1.py:183(test_3)
#        69    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        76    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
# ----------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('test_3(begin, 250, row, result)')
# ---------------------------------------------
# 464 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 homework_4.1.py:183(test_3)
#       219    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       241    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
# ----------------------------------------------------------------------------------------------


# ---------------------------------------------
# cProfile.run('test_3(begin, 500, row, result)')
# ---------------------------------------------
# 989 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 homework_4.1.py:183(test_3)
#       469    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       516    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
# ----------------------------------------------------------------------------------------------



# ---------------------------------------------
# cProfile.run('test_3(begin, 1000, row, result)')
# ---------------------------------------------

# 2039 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.001    0.001    0.002    0.002 homework_4.1.py:183(test_3)
#       969    0.000    0.000    0.000    0.000 {built-in method builtins.chr}
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1066    0.001    0.000    0.001    0.000 {method 'format' of 'str' objects}
