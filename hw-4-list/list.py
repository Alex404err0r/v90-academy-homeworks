# 1
list = ["First", "", "Third", " ", "Fourth", " "]
list[:] = [x for x in list if x.strip()]
print(list)


# 2
list = [2, 3, 5]
s = list
x = [int(i)**2 for i in s]
print(x)


# 3
list = [22, 23, 20, 28, 20, 21, 20]
for i in list:
	if i==20:
		list.remove(i)
print(list)


# 4
s = [5, 4, 3, 2, 1]
a = [int(i) for i in s[::-1]]
print(a)


#5
l = [4, 2, 3, 1]

maximum = max(l)
minimum = min(l)

for i in range(len(l)):
	if l[i] == maximum:
	  l[i] = minimum
	elif l[i] == minimum:
		l[i] = maximum
print(l)


#6
l = [1, 2, 3, 2, 5, 4, 1]
print(*filter(lambda x : l.count(x) > 1, l))


