a, b = int(input()), int(input())
s=0 # сумма всех чисел кратных 3 в диапазоне
x=0 # переменная для подсчета количества цифр в диапазоне
for i in range(a,b+1):
    if i % 3 == 0:
        x += 1
        s += i
        print (i,end=" ")
print ()
print (s)
print (x)
print (s/x)
# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b],
# которые делятся на 3.
#
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12].
# Всего чисел, делящихся на 3, на этом отрезке 6: -3, 0, 3, 6, 9, 12.
# Их среднее арифметическое равно 4.5
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число,
# которое делится на 3.

