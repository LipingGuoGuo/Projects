# python传参数是传值还是传址
# python 中函数参数是引用传递（注意不是值传递）
# 对于不可变类型（数值型，字符串，元祖），因变量不能修改，所以运算不会影响到变量自身
# 对于可变类型（列表，字典）来说，函数体运算可能会更改传入的参数变量
def selfAdd(a):
    a += a

a_int = 1
print(a_int)
selfAdd(a_int)
print(a_int)


a_list = [1,2]
print(a_list)
selfAdd(a_list)
print(a_list) 