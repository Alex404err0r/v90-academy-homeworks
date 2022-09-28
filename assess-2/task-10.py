from collections import Counter

inp = 'file.txt'
letters = 0
lines = 0
words = 0

for line in open(inp):
	lines += 1
	letters += len(line)


	p = 'out'
	for letter in line:
	    if letter != '!' and p =='out':
               words += 1
               p = 'in'
	    elif letter == ' ':
	        p = 'out'

file = open(inp)
counter = Counter(file.read().lower())
rare_letter = min(counter, key=counter.get)
file.close()

print(f'Количество букв в файле: {letters}')
print(f'Колличество строк в файле: {lines}')
print(f'Колличество слов в файле: {words}')
