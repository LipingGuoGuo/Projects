# python中copy和deepcopy区别
# 复制不可变数据类型，都是同一个地址当浅复制的值是不可变对象（数值，字符串，元组）时和=的情况一样。对象的id值与浅复制原来的值相同
# 复制的值时可变对象（列表和字典）
import copy

a = "哈哈"
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))
