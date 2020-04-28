a, b = int(input()), int(input())
c, d = int(input()), int(input())
print(end ="\t")
print(*range(c,d+1),sep='\t')
for i in range(a,b+1):
    print(i, end ="\t")
    for j in range(c,d+1):
        for g in range (1):
            print(i*j, end="\t")
    print()



# a, b = int(input()), int(input())
# c, d = int(input()), int(input())
# print('\t', end = '')
# for q in range(c, d+1):
#     print(q, end='\t')
# print()
# for i in range(a,b+1):
#     print(i, end ="\t")
#     for j in range(c,d+1):
#         for g in range (1):
#             print(i*j, end="\t")
#     print()

# a, b = int(input()), int(input())
# c, d = int(input()), int(input())
# for i in range(a,b+1):
#     print(i, end ="\t")
#     for j in range(c,d+1):
#         for g in range (1):
#             print(i*j, end="\t")
#     print()
# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
# Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.

# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b] на все числа
# отрезка [c;d]. Числа a, b, c и d являются натуральными и непревосходят 10, a≤b, c≤d.

# Следуйте формату вывода из примера, для разделения
# элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым
# столбцом и верхней строкой выводятся сами числа из заданных отрезков —
# заголовочные столбец и строка таблицы.