# Задание № 1

lst = [1, 2, 3, 4, 5, 6, 7]
s = 0
for x in lst:
	s += x
print("Сумма списка for:")
print(s)

list_length = len(lst)
sum = 0
count = 0

while count < list_length:
	sum = sum + lst[count]
	count = count + 1
print("Сумма спика while:")
print(sum)