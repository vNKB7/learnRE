#!/usr/bin/env python3

import re
'''
tips
1.在模式中使用原始字符串让raw strings: r'xxx'


'''



# group和groups的用法。括号的功能：保存为子组。
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())

'''
abc-123
abc
123
('abc', '123')
'''

print('-------------------')
# 子组进阶
m = re.match('ab', 'ab')
print(m.group())
print(m.groups())

'''
ab
()
'''

m = re.match('(a(b))(c)', 'abc')
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

'''
abc
ab
b
c
('ab', 'b')
'''

print('-------------------')
#findall()--用于非重叠地搜索某字符串中一个模式出现的情况。findall()会返回一个列表。如果没有匹配，则返回空列表。
print(re.findall('abc', 'abcdabceabcf'))
'''
['abc', 'abc', 'abc']
'''

print(re.findall('(a(b(c)))', 'abcdabceabcf'))
'''
[('abc', 'bc', 'c'), ('abc', 'bc', 'c'), ('abc', 'bc', 'c')]
如果有多个子组，对于每一个匹配，对应一个元组，在元组中列出子组的所有匹配。
'''

print('-------------------')
# sub(), subn() 替换
print(re.sub('a', 'b', 'aaa'))


print('-------------------')
# split()

