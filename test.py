# -*- coding: utf-8 -*-
import re

TET = open('TET.txt', 'r', encoding='unicode_escape')
result = open('result.txt', 'w')
'''
txt=TET.readline()
print(txt)
print(type(txt))
result.write(txt)
'''
txt = TET.read().encode('unicode_escape')
print(type(txt))
result.write(str(txt))
TET.close()
result.close()
