# -*- coding: utf-8 -*-

first_name = "ada"
last_name = "lovelace"
# 引号中的空格是为了打印姓名时在姓与名中添加空格
full_name = first_name + " " + last_name

# 如果不加空格姓名中也不会有空格
full_name1 = first_name + last_name

# 也可以直接将函数写入新变量，这样最后的执行语句会更简单
message = "Hello, " + full_name.title() + "!"

print(full_name)
print(full_name1)
# “.”加在变量full_name后面是为了引用函数，
print("Hello, " + full_name.title() + "!")
print(message)
