# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2,
# первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.


fib = [1, 2]                                 # Создали список из двух начальных значений

while fib[-1] < 4000000:                     # Пока последнее элемент не больше 4 миллионов цикл не завершиться
    fib.append(fib[-2] + fib[-1])            # добавляем в список сумму предпоследнего и последнего элемента
result = filter(lambda x: x % 2 == 0, fib)   # ищем все четные числа в списке

if __name__ == '__main__':
    print(sum(result))
