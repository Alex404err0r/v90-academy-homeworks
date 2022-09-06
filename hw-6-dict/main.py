# 1
dictionary_1 = {'a': 300, 'b': 400}
dictioanry_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictioanry_2)
print(dictionary_1)
print()

#3
d = {i : i ** 3 for i in range(1, 11)}
print(d)
print()

#4
k = ['fruit', 'vegetable', 'berry']
v = ['avocado', 'potatoes' , 'raspberry']
scroll_d = dict(zip(k, v))
print(scroll_d)
print()

#5
str = 'triviialis'
dict = {i: str.count(i) for i in str}
print(dict)