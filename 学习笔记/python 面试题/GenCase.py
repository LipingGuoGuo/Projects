# 请将[i for i in range(3)]改成生成器
# 生成器是特殊的迭代器
# 列表表达式的[]改为（）即可变成生成器
# 函数在返回值的时候出现yield 就变成生成器，而不是函数
a = (i for i in range(3))
print(type(a))