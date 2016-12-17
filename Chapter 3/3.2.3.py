# -*- coding: utf-8 -*-

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# pop() 用来删除列表最后一个元素，可在括号中添加索引来删除指定位置的元素
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# 当不知道元素的位置，只知道元素的值的时候，可以用 remove()，remove只删除第一个出现的指定值
motorcycles.remove('ducati')
print(motorcycles)
