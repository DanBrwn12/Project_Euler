# Дано:
# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
# Алгоритм работы:
# 1.Нам нужен пустой список в который мы будем заносить наши простые делители
# 2.Зададим наше число в переменную, чтобы постоянно не писать большое число
# 3.Нужно создать цикл, который будет во всем диапозоне от 2 (т.к. 1 не простое число) до нашего
# числа искать кратные ему числа.
# 4. Когда наш цикл дойдет до заданного числа, прекратить
# 5. Вывести максимальное число из нашего списка

div = []
a = 600851475143
count = 1

for i in range(70, a + 1):
    if a % i == 0:
        a = a / i
        div.append(i)
        print(i, end=', ')
    if count == a:
        print('the end')
        break

if __name__ == '__main__':
    assert div == [71, 839, 1471, 6857]
    assert max(div) == 6857