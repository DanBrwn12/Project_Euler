'''Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?'''
import math
number = 600000
count = 1
easy_div = [2]
for i in range(3, number, 2):
    if i > 10 and i % 10 == 5:
        continue
    for j in range(2, i):
        if j > int((math.sqrt(i)+ 1)):
            easy_div.append(i)
            break
        if i % j == 0:
            break

        # if easy_div[10001]:
        #     print(easy_div[10001])
        #     break
    else:
        easy_div.append(i)

print(easy_div[10001])
