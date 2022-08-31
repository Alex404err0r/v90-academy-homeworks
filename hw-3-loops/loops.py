from collections import defaultdict

str = 'Определить количество вхождений символа в строку!'

chars = defaultdict(int)

for char in str:
  chars[char] +=1

print('1-->', chars['о'] + chars['О'])