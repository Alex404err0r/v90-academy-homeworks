# Задание номер № 2

a = [1, 2, 3]
b = [11, 22, 33]

min_1, max_1 = sorted([a, b], key=len)

c = list()
for x in range(len(min_1)):
 c.extend([a[x], b[x]])

c.extend(sorted(max_1[len(min_1):]))
print('Третий список: ', c)


s = [1, 2, 3] #2 зная второй список, не записав значение
s2 = [11, 22, 33]
s.insert(1, 11)
s.insert(3, 22)
s.insert(5, 33)
print(s)