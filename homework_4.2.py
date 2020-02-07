import cProfile
import timeit


# ВЫВОД:
# 1. Первый алгоритм(Решето Эратосфена) отрабатывает быстрее второго алгоритма.
# 2. Второй алгоритм(Без решета) отрабатывает дольше первого алгоритма


# ============= 1 вариант ================ Решето Эратосфена
n = 5000
massive = [i for i in range(n)]
massive[1] = 0
k = 0
res = []

def sieve(a):
    global res
    for i in range(2, n):
        if massive[i] != 0:
            x = i + i
            while x < n:
                massive[x] = 0
                x += i
        res = [i for i in massive if i != 0]
    # print(res)
    return res[a-1]

print(sieve(5))

# print(timeit.timeit('sieve(100)', number=100, globals=globals()))           #   96.84000738099999
# print(timeit.timeit('sieve(200)', number=100, globals=globals()))           #   99.71505610999999
# print(timeit.timeit('sieve(300)', number=100, globals=globals()))           #   98.86625028399999
# print(timeit.timeit('sieve(400)', number=100, globals=globals()))           #   98.982961058
# print(timeit.timeit('sieve(500)', number=100, globals=globals()))           #   98.36205564200003
# =================================================================================================

# ==========================
# cProfile.run('sieve(100)')
# ==========================
# 5002 function calls in 0.932 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.932    0.932 <string>:1(<module>)
#         1    0.014    0.014    0.932    0.932 homework_4.2.py:11(sieve)
#      4998    0.918    0.000    0.918    0.000 homework_4.2.py:19(<listcomp>)
#         1    0.000    0.000    0.932    0.932 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ==============================================================================================


# ==========================
# cProfile.run('sieve(200)')
# ==========================
# 5002 function calls in 0.963 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.963    0.963 <string>:1(<module>)
#         1    0.015    0.015    0.963    0.963 homework_4.2.py:11(sieve)
#      4998    0.948    0.000    0.948    0.000 homework_4.2.py:19(<listcomp>)
#         1    0.000    0.000    0.963    0.963 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ==============================================================================================


# ==========================
# cProfile.run('sieve(300)')
# ==========================
# 5002 function calls in 0.940 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.940    0.940 <string>:1(<module>)
#         1    0.015    0.015    0.940    0.940 homework_4.2.py:11(sieve)
#      4998    0.925    0.000    0.925    0.000 homework_4.2.py:19(<listcomp>)
#         1    0.000    0.000    0.940    0.940 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ==============================================================================================


# ==========================
# cProfile.run('sieve(400)')
# ==========================
# 5002 function calls in 0.920 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.920    0.920 <string>:1(<module>)
#         1    0.014    0.014    0.920    0.920 homework_4.2.py:11(sieve)
#      4998    0.906    0.000    0.906    0.000 homework_4.2.py:19(<listcomp>)
#         1    0.000    0.000    0.920    0.920 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ==============================================================================================

# ==========================
# cProfile.run('sieve(500)')
# ==========================
# 5002 function calls in 0.934 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.934    0.934 <string>:1(<module>)
#         1    0.013    0.013    0.934    0.934 homework_4.2.py:11(sieve)
#      4998    0.921    0.000    0.921    0.000 homework_4.2.py:19(<listcomp>)
#         1    0.000    0.000    0.934    0.934 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ================================================================================================

print('='* 80)

# ============= 2 вариант ================ Без решета Эратосфена

def prime(a):
    global k, n
    for i in range(2, n):
        for x in range(2, i):
            if i % x == 0:
                k = k + 1
        if k == 0:
            res.append(i)
        else:
            k = 0
    print(res)
    return res[a-1]

print(prime(10))


# print(timeit.timeit('prime(100)', number=100, globals=globals()))               #       104.194781979
# print(timeit.timeit('prime(200)', number=100, globals=globals()))               #       107.09083874199999
# print(timeit.timeit('prime(300)', number=100, globals=globals()))               #       105.456675305
# print(timeit.timeit('prime(400)', number=100, globals=globals()))               #       110.889832904
# print(timeit.timeit('prime(500)', number=100, globals=globals()))               #       110.81023481600005


# ==========================
# cProfile.run('prime(100)')
# ==========================
# 674 function calls in 1.061 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.061    1.061 <string>:1(<module>)
#         1    1.058    1.058    1.061    1.061 homework_4.2.py:116(prime)
#         1    0.000    0.000    1.061    1.061 {built-in method builtins.exec}
#         1    0.003    0.003    0.003    0.003 {built-in method builtins.print}
#       669    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ==============================================================================================

# ==========================
# cProfile.run('prime(200)')
# ==========================
# 674 function calls in 1.036 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.036    1.036 <string>:1(<module>)
#         1    1.034    1.034    1.036    1.036 homework_4.2.py:116(prime)
#         1    0.000    0.000    1.036    1.036 {built-in method builtins.exec}
#         1    0.002    0.002    0.002    0.002 {built-in method builtins.print}
#       669    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ===============================================================================================


# ==========================
# cProfile.run('prime(300)')
# ==========================
# 674 function calls in 1.037 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.037    1.037 <string>:1(<module>)
#         1    1.031    1.031    1.037    1.037 homework_4.2.py:116(prime)
#         1    0.000    0.000    1.037    1.037 {built-in method builtins.exec}
#         1    0.006    0.006    0.006    0.006 {built-in method builtins.print}
#       669    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# =================================================================================================


# ==========================
# cProfile.run('prime(400)')
# ==========================
# 674 function calls in 1.052 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.052    1.052 <string>:1(<module>)
#         1    1.048    1.048    1.052    1.052 homework_4.2.py:116(prime)
#         1    0.000    0.000    1.052    1.052 {built-in method builtins.exec}
#         1    0.004    0.004    0.004    0.004 {built-in method builtins.print}
#       669    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ===============================================================================================


# ==========================
# cProfile.run('prime(500)')
# ==========================
# 674 function calls in 1.044 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.043    1.043 <string>:1(<module>)
#         1    1.041    1.041    1.043    1.043 homework_4.2.py:116(prime)
#         1    0.000    0.000    1.044    1.044 {built-in method builtins.exec}
#         1    0.002    0.002    0.002    0.002 {built-in method builtins.print}
#       669    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# ===============================================================================================