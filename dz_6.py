# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN
# N может быть любой длины.
def zadacha_1():
  number = int(input("Введите число N: "))
  temp = str(number)
  n1 = temp + temp
  n2 = temp + temp + temp
  result = number + int(n1) + int(n2)
  print("Результат равен:", result)
#-----------------------------------------------
# Задача 2. Задан массив из случайных цифр на 15 элементов.На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в # массиве последовательность из трёх элементов, совпадающая с введённым числом.
from random import randint
list_1 = list([randint(0,10) for i in range(15)])
print(list_1)
x = int(input("Введите проверяемое число от: "))
count = 0
for i in list_1:
    if x == i:
        count+=1
print(f'В данном массиве число {x} встречается {count} раз')