# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint
n = int(input('Введите количество монет лежащих на столе: '))
# print('Введите положение монеты 1 - решка, 0 - орел: ')
k = 0
coin_position = []
for i in range(n):    
    coin_position.append(randint(0, 1))
print(n, "->", coin_position)
null = coin_position.count(0) 
if len(coin_position) - null < null:
    print(len(coin_position) - null)
else:
     print(null)

