# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# x + y = S ---> x = S - y
# xy = y(S-y) = P ---> y^2 - Sy + P = 0 - надо решить квадратное уравнение



s = int(input('Введите сумму двух чисел S: '))
p = int(input('Введите произведение двух чисел P: '))
d = s**2 - 4*p # находим дискриминант
if d == 0:
    print(round(s/2), round(s/2))
elif d > 0:
    print(round((s - d)/2), round((s + d)/2))
elif d < 0:
    print('таких чисел нет!')
