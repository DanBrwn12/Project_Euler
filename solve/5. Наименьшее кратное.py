'''Дано:
2520 - самое маленькое число, которое делитеся без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
АЛГОРИТМ РАБОТЫ:
1) нужно создать цикл который будет перебирать все числа от 2520 и делить их по очереди нацело на числа от 1 до 20
2) как только это число найдется, вывести его на экран'''


import time
def smallest_mult(num_period):
    start_time, result, multipliers = time.time(), 6, [1, 2, 3]
    for number in range(4, num_period+1):
        for multip in multipliers:
            if number % multip == 0:
                number = number / multip
        multipliers.append(number)
        result *= number
    print(result, "--- %s seconds ---" % (time.time() - start_time), sep="\n")
smallest_mult(num_period=20)

