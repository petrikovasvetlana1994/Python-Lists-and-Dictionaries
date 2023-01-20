'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
'''
N = int(input("введите количество элементов массива: "))
A = list(map(int, input("введите числа в массиве через пробел одной строкой: ").split()))
X = int(input("введите число: "))
Z = [abs(A[i]-X) for i in range(len(A))]
print(A[Z.index(min(Z))])

""" или
n = int(input())

# list1 = list()
# for i in range(n):
#     list1.append(int(input()))

list1 = [int(input()) for i in range(n)]
k= int(input())

m = abs(k - list1[0])
number = list1[0]

for i in range(1, len(list1)):
    if m > abs(k - list1[i]):
        m = abs(k - list1[i])
        number = list1[i]

print(number)
"""