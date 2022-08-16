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

# 2.1#
str = "Текстовый пример"
print("2.1", "Текстовый" in "пример")
str = "Текстовый пример"
string = str.find("Текстовый документ")
print("2.2", string)

# 3#
str = "Текстовый пример"
print("3", 'str'.count(str))
str = 'Текстовый пример'.count('Пример текста')
print("3.1", str)

# 4#
string = "Текстовый пример!"
print("4", string.find("Т"))
print("4.1", string.find("!"))

# 5#
string = "А роза упала на лапу Азора"
def IsPalindrome(string):
	if len(string) <=1:
		return True
	else:
		return string[0] == string[-1] and IsPalindrome(string[1:-1])
print("5", IsPalindrome(string))