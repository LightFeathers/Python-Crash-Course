# -*- coding: utf-8 -*-

numbers = list(range(1,6))
print(numbers)

# range(2,11,2) 中的2、11、2分别表示从数字'2'开始，到数字'11'前，每次加2
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2    # **n 表示赋值为n次方，
    squares.append(square)

print(squares)

# 更Pythonic的写法
squares = []
for value in range(1,11):
    squares.append(value**2)    # 把上一个写法进行了合并
print(squares)
