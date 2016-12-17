# -*- coding: utf-8 -*-

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 在列表中添加元素，append 会将新元素添加在列表末尾
motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
# insert() 可以在列表中指定位置添加新元素
motorcycles.insert(0, 'ducati')
print(motorcycles)
