# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('Введите целое положительное число: '))
p_list = []
pow = 1
power = 1
while pow <= n:
    p_list.append(pow)
    pow = 2 ** power
    power += 1
print(n, '->', *p_list)