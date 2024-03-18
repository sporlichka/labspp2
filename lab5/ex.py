# p = re.compile('[+][1-9][0-9]{0,2}([(][0-9]{3}[)]|[ ][0-9]{3}[ ]|[0-9]{3})([0-9]{3}[ -]?[0-9]{2}[ -]?[0-9]{2})')
# m = p.search(r'+102 777 777-77-77')
# print(m.group())
import re
# 5
s = str(input())
p = re.compile('a.*?b$')
m = p.search(s)
print(m)