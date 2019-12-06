a, b, c = int(input()), int(input()), int(input())
a = (a + b + c) - (b + c)
b = (a + b + c) - (a + c)
c = (a + b + c) - (a + b)
if b == c == a:
    print(a, b, c, sep="\n")
if a > b > c:
    print(a, c, b, sep="\n")
if a > c > b:
    print(a, b, c, sep="\n")
if a == c > b:
    print(a, b, c, sep="\n")
if a == c < b:
    print(b, a, c, sep="\n")
if a == b > c:
    print(a, c, b, sep="\n")
if a == b < c:
    print(c, a, b, sep="\n")
if b > a > c:
    print(b, c, a, sep="\n")
if b > c > a:
    print(b, a, c, sep="\n")
if b == c > a:
    print(b, a, c, sep="\n")
if b == c < a:
    print(a, b, c, sep="\n")
if c > a > b:
    print(c, b, a, sep="\n")
if c > b > a:
    print(c, a, b, sep="\n")

# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки сначала максимальное,
# потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.
