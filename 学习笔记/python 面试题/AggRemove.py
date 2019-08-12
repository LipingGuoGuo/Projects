# 题目4：python实现列表去重的方法
# 先通过集合去重，再转列表
list = [11,12,13,15,16,13]
a = set(list)
print(a)

list1 = [x for x in a]
print(list1)