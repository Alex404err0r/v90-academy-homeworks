# Задание № 3

num = int(input("Введите целое число: "))
sum = 0
while (num != 0):
  sum = sum + num % 10
  num = num // 10
print("Cумма: ", sum)