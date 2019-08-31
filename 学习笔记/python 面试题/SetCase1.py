# 集合是由不重复元素组成的无序的集
# 集合对象也支持像联合，交集，差集，对称差分等数学运算
# 花括号或set()函数可以用来创建集合
# 创建一个空集合只能用set()而不可用{}，后者是创建一个空字典
a = set('avdgdgaaasd')
b = set('agsbbssss')
print(a)
print(b)
# 存在a不存在b中的元素
print(a-b)
# a,b并集
print(a|b)
# a,b交集
print(a&b)
# 存在a或b但非公共
print(a^b)