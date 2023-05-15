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
  array = list([randint(0,100) for i in range(15)])
  print(array)
  array = (''.join(map(str, array)))
  nunber = input('Введите трехзначное число:')
  lenght_number = len(nunber)
  lenght_array = len(array)
  count = 0
  for i in range(lenght_array):
    if array[i:i+lenght_number] == nunber:
      count+=1
  if count > 0:
    print(f'В массиве  ЕСТЬ совпадение из последовательности чисел "{nunber}"')
    print(f'Колличество совпадений с введенным числом: {count} раз(-а)')
  else:
   print(f'В массиве  НЕТ совпадений из последовательности чисел {nunber}') 
#Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
from math import gcd
def Task3():
    print("\nЗадача 3:")
    max_denominator = 11
    fractions = simple_fractions(max_denominator)
    print("Несократимые дроби между 0 и 1 с знаменателем не больше", max_denominator)
    for fraction in fractions:
        print(f"{fraction[0]}/{fraction[1]}")

def is_coprime(a, b):
    return gcd(a, b) == 1

def simple_fractions(max_denominator):
    fractions = []
    for denominator in range(1, max_denominator + 1):
        for numerator in range(1, denominator):
            if is_coprime(numerator, denominator):
                fractions.append((numerator, denominator))
    return fractions
Task3()
