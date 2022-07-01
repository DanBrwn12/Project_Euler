# ДАНО
# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
# АЛГОРИТМ РАБОТЫ:
# 1. Нужно создать цикл, в котором будет осуществляться умножение сначала одного трехзначного числа на последовательность трехзначных чисел
# другого, затем с прибавлением первого числа на 1, будет осуществляться повторное умножение
# 2. далее произвести проверку всех полученных результатов на полиндром путем создания функций:
# 1) которая будет переворачивать наше число
# 2) которая будет проверять равно ли перевернутое число исходному
# 3) если равно, то вывести на экран
# 4. Скорее всего лучше создать декоратор для цикла, чтобы не писать этот цикл несколько раз

def multiply():
    for i in range(100, 999):
        for j in range(100, 999):
            mult = i * j
            j +=1
            if i == 999:
                j +=1
            string = str(mult)
            if string == string[::-1]:
                arr =[]
                arr.append(string)
    print(arr[-1])

if __name__ == '__main__':
    multiply()

