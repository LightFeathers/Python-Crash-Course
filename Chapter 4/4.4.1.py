# -*- coding: utf-8 -*-

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# [0:3]中间不是逗号而是冒号，另外同range()一样也是类似于[0,3)的意思
print(players[0:3])

# 如果没有指定起始索引，将从开头开始
print(players[:3])

# 同理，如果没有指定末尾索引，将一直提取到最后一个元素
print(players[2:])

# 如果起始元素为-n,即从倒数第n个数开始到结尾
print(players[-3:])
