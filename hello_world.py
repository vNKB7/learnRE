#!/usr/bin/env python3

import re

# match
m = re.match('foo', 'foo1')
if m:
    print(m.group())
else:
    print('None')

m = re.match('foo', 'bar')
if m:
    print(m.group())
else:
    print('None')

m = re.match('foo', 'notfoo')
if m:
    print(m.group())
else:
    print('None')


'''
即使字符串比模式长，也可以匹配成功。只要模式从字符串开头有一个成功的匹配。

if虽然可以省略，但有时候会产生AttributeError异常，因为m可能为None。
'''

# search

m = re.search('foo', 'seafood')
if m:
    print(m.group())







