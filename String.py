string = 'Текстовый пример'

# 1.1#
print("1.1", string[2])
# 1.2#
print("1.2", string[-2])
# 1.3#
print("1.3", string[:5])
# 1.4#
print("1.4", string[:-2])
# 1.5#
print("1.5", string[::2])
# 1.6#
print("1.6", string[1::2])
# 1.7#
print("1.7", string[::-1])
# 1.8#
print("1.8", string[::-2])
# 1.9#
print("1.9", len(string))

# 2#
if sorted('eat') == sorted('tea'):
	print('2', 'Строки являются анаграммами.')
else:
	print('2', 'Строки не являются анаграммами.')

# 3#
str = "ТеКсТоВыЙ ПрИмЕр!"
count = 0
for i in str:
	if i == "е":
		count = count +1
for i in str:
	if i == "Е":
		count = count +1
print('3', count)

#3.1#
str = "ТеКсТоВыЙ ПрИмЕр!"
st = str.lower()
count = 0
for i in st:
	if i == "е":
		count = count +1
print('3.1', count)

#3.2#
str = "ТеКсТоВыЙ ПрИмЕр!"
count = 0
for i in str:
	if i == "!":
		count = count + 1
print('3.2', count)

# 4#
st = 'www.python.org'
print ('4', st.find('.'), st.rfind('.'))# как вариант мб

#4.1#
from collections import defaultdict #c подкл. класса'2' модуля'1'
st = 'Ситуации бывают лёгкими,\
     средними, трудными и паршивыми,\
     но вот безвыходных я пока не встречал.'
chars = defaultdict(int)

for char in st:
	chars[char] +=1
print('4.1', chars[','])
print('4.2', chars['а'])

# 5#
string = "А роза упала на лапу Азора"
def IsPalindrome(string):
	if len(string) <=1:
		return True
	else:
		return string[0] == string[-1] and IsPalindrome(string[1:-1])
print("5", IsPalindrome(string))

#5.1#
def polin(s):
	s = s.lower()
	wrong = ['.', ',', ' ', '!', '?', '-', ':']
	for symbol in wrong:
		s = s.replace(symbol, '')
		return s != s[::-1]

print('5.1', polin('Он дивен, палиндром — и ни морд, ни лап не видно.'))