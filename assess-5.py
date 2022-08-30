# Задание № 1

# lst = [1, 2, 3, 4, 5, 6, 7]
# s = 0
# for x in lst:
# 	s += x
# print("Сумма списка for:")
# print(s)
#
# list_length = len(lst)
# sum = 0
# count = 0
#
# while count < list_length:
# 	sum = sum + lst[count]
# 	count = count + 1
# print("Сумма спика while:")
# print(sum)



# Задание номер № 2

# a = [1, 2, 3]
# b = [11, 22, 33]
#
# min_1, max_1 = sorted([a, b], key=len)
#
# c = list()
# for x in range(len(min_1)):
#  c.extend([a[x], b[x]])
#
# c.extend(sorted(max_1[len(min_1):]))
# print('Третий список: ',c)


# s = [1, 2, 3] #2 зная второй список, не записав значение
# s2 = [11, 22, 33]
# s.insert(1, 11)
# s.insert(3, 22)
# s.insert(5, 33)
# print(s)



# Задание № 3

# num = int(input("Введите целое число: "))
# sum = 0
# while (num != 0):
#   sum = sum + num % 10
#   num = num // 10
# print("Cумма: ", sum)



# Задание № 4

# import math
#
# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
#
# if discr > 0:
# 	x1 = (-b + math.sqrt(discr)) / (2 * a)
# 	x2 = (-b - math.sqrt(discr)) / (2 * a)
# 	print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
# 	x = -b / (2 * a)
# 	print("x = %.2f" % x)
# else:
# 	print("Корней нет")



# Задание № 5
# n = 4
# f = 1
# for i in range(2, n+1):
# 	f = f * i
# print("Факториал числа",n, ":", f)



# Задание № 6

# s = [1, 2, 3]
# s2 = [4, 5, 6]
# s.extend(s2)

# print(s)
# num = [1, 2, 3, 5, 1, 2, 6, 7]
# print(num)



# Задание № 8

# from random import randint
#
# N = 10
# a = []
# for i in range(N):
#  a.append(randint(1, 47))
# print (a)
#
# for i in range(N-1):
#  for j in range(N-i-1):
# 		if a[j] > a[j+1]:
# 			a[j], a[j+1] = a[j+1], a[j]
# print(a)