# 1
a = ('Time is money ')
b = ('No money - no honey.')
c = []


for i in a:
	for j in b:
		if i == j:
			c.append(i)

			break

print(c)
print()


# 2
from collections import Counter
str = 'Life is series of choices.'
s = tuple(str)
print(dict(Counter(s)))
print()


# 3
temp = (24, 25, 24, 23, 25, 23, 20)
sum_temp = (sum(temp))
days = 7
mean_temp = sum_temp / days
print('Средня температура за неделю: ', int(mean_temp))
