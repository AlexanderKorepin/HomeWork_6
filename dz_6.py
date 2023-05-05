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
def zadacha_3():
  array = list([randint(0,2) for i in range(15)])
  array = (''.join(map(str, array)))
  print(array)
  nunber = input('Введите трехзначное число:')
  lenght_number = len(nunber)
  lenght_array = len(array)
  count = 0
  for i in range(lenght_array):
    if array[i:i+lenght_number] == nunber:
      count+=1
  if count > 0:
    print(f'В массиве  "{array}" ЕСТЬ совпадение из последовательности чисел "{nunber}"')
    print(f'Колличество совпадений с введенным числом: {count} раз(-а)')
  else:
   print(f'В массиве  {array} НЕТ совпадений из последовательности чисел {nunber}') 
zadacha_3()


